#region CUSTOMISATION

TOKEN = "7511843239:AAGnd7fcEYmrhWqs1MnvD3EKm41VXK2YuI4"

SAVE_FILE = "quiz_state.json"
LOAD_SAVE_FILE = True
#RESET_SAVE_FILE = False

GROUP_ALLOCATION = ["random", "in_order", "fill_up"]
GROUP_ALLOCATION_MODE = GROUP_ALLOCATION[1]

STAGE_ALLOCATION = ["predefined", "dynamic"]
STAGE_ALLOCATION_MODE = STAGE_ALLOCATION[1]

QUESTION_SEQUENCING = ["1b1", "2b2"]
QUESTION_SEQUENCING_MODE = QUESTION_SEQUENCING[1]

CORRECT_SCORE = 20
WRONG_SCORE = -10

MAX_STAGES = 5

MAX_GROUPS = 7
MAX_PER_GROUP = 2

ADMIN_CHAT_ID = -4865327027


#endregion

#region IMPORTS

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import random
import asyncio
from typing import Optional

import os
import json


from telegram.ext import Defaults
from telegram.constants import ParseMode
from telegram.ext import AIORateLimiter
from telegram.request import HTTPXRequest
from telegram.error import RetryAfter
from collections import defaultdict

import random
import time
from datetime import datetime


from telegram.ext import JobQueue


chat_locks = defaultdict(asyncio.Lock)



#endregion

#region RATE LIMITING

request = HTTPXRequest(
    read_timeout=20,
    write_timeout=20,
    connect_timeout=8,
    pool_timeout=15,
    connection_pool_size=100,  # Reduced from 200
)

defaults = Defaults(parse_mode=ParseMode.HTML)

question_send_semaphore = asyncio.Semaphore(10)

RATE_LIMIT_DELAY = 0.1
MAX_CONCURRENT_REQUESTS = 15
rate_limit_semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

onboarding_semaphore = asyncio.Semaphore(10) 

from telegram.error import RetryAfter, NetworkError
import random
import asyncio

async def safe_send(func, *args, max_retries=5, **kwargs):
    """Enhanced safe send with rate limiting, retry, and network error handling."""
    for attempt in range(max_retries):
        try:
            async with rate_limit_semaphore:
                # Add jitter to prevent thundering herd
                jitter = random.uniform(0, RATE_LIMIT_DELAY)
                await asyncio.sleep(RATE_LIMIT_DELAY + jitter)
                
                return await func(*args, **kwargs)

        except RetryAfter as e:
            if attempt == max_retries - 1:
                print("❌ Max retries exceeded due to rate limiting.")
                raise

            wait_time = e.retry_after + random.uniform(1, 3)
            print(f"⚠️ Rate limited — retrying in {wait_time:.1f}s (attempt {attempt + 1})")
            await asyncio.sleep(wait_time)

        except NetworkError as e:
            if attempt == max_retries - 1:
                print(f"❌ NetworkError after {max_retries} retries: {e}")
                raise

            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"🌐 Network error — retrying in {wait_time:.1f}s (attempt {attempt + 1}): {e}")
            await asyncio.sleep(wait_time)

        except Exception as e:
            if attempt == max_retries - 1:
                print(f"❌ Failed after {max_retries} attempts: {e}")
                raise

            wait_time = (2 ** attempt) + random.uniform(0, 1)
            print(f"⚠️ Error — retrying in {wait_time:.1f}s (attempt {attempt + 1}): {e}")
            await asyncio.sleep(wait_time)

    # Should never get here
    raise RuntimeError("safe_send failed unexpectedly")

#endregion

#region ALL DATA

#region GROUP INTERFACE

#region GROUP IDS

GROUP_CHAT_IDS_NUMBERS = {
    "-1002889743741" : 1,
    "-1002895190043" : 2,
    "-1002607909232" : 3,
    "-1002592316801" : 4,
    "-1002689435140" : 5,
    "-1002813761428" : 6,
    "-1002887568054" : 7
}

ALL_CHAT_IDS = GROUP_CHAT_IDS_NUMBERS.keys()

async def get_group_number(update=None, context=None, chat_id=None):
    if chat_id is None:
        if context is None:
            chat_id = update.effective_chat.id
        elif update is None:
            chat_id = context.chat_data["chat_id"]

    group_number = GROUP_CHAT_IDS_NUMBERS[chat_id]

    return group_number

#endregion

#region GROUP LINKS

GROUP_LINKS = {
    1: "https://t.me/+A5qVDOpiD3tiOWRl",
    2: "https://t.me/+VyBtzuTtygNmYTE1",
    3: "https://t.me/+IP3busCPh7AwZTQ1",
    4: "https://t.me/+GlcPvOQYrLUwOThl",
    5: "https://t.me/+GZ8jrg7YEIU0OTJl",
    6: "https://t.me/+vIs68K-wfv42ZTE1",
    7: "https://t.me/+xUa4NVmen2xiZjA9"
}

async def get_group_link(context=None, group_number=None):
    if group_number is None:
        group_number = context.user_data["group_number"]

    group_link = GROUP_LINKS[group_number]

    return group_link

#endregion

#region GROUP ALLOCATION

ORDERED_GROUP_INDEX = 1
GROUP_POPULATION = 0
group_index_lock = asyncio.Lock()

async def set_group_number(context):
    global ORDERED_GROUP_INDEX
    global GROUP_POPULATION

    if GROUP_ALLOCATION_MODE == "random":
        group_number = random.randint(1, MAX_GROUPS)
    
    elif GROUP_ALLOCATION_MODE == "in_order":
        async with group_index_lock:
            group_number = ORDERED_GROUP_INDEX
            ORDERED_GROUP_INDEX = (ORDERED_GROUP_INDEX % MAX_GROUPS) + 1

    elif GROUP_ALLOCATION_MODE == "fill_up":

        async with group_index_lock:
            group_number = ORDERED_GROUP_INDEX
            GROUP_POPULATION += 1

            if GROUP_POPULATION == MAX_PER_GROUP:
                if ORDERED_GROUP_INDEX <= MAX_GROUPS:
                    ORDERED_GROUP_INDEX += 1
                    GROUP_POPULATION = 0

    context.user_data["group_number"] = group_number

    return group_number

#endregion

#endregion

#region QUESTION INTERFACE

#region QUESTION DATA

ALL_STAGE_QUESTIONS = {
    1: {
        "A": {
            1: {
                1: {"question": "E1PAS1 What is 1 + 1?", "options": ["1", "2", "3"], "answer": "2"},
                2: {"question": "E1PAS1 What is 1 + 2?", "options": ["2", "3", "4"], "answer": "3"},
            },
            2: {
                1: {"question": "E1PAS2 What is 1 + 3?", "options": ["3", "4", "5"], "answer": "4"},
                2: {"question": "E1PAS2 What is 1 + 4?", "options": ["4", "5", "6"], "answer": "5"},
            }
        },
        "B": {
            1: {
                1: {"question": "E1PBS1 What is 1 - 0?", "options": ["0", "1", "2"], "answer": "1"},
                2: {"question": "E1PBS1 What is 1 - 1?", "options": ["-1", "0", "1"], "answer": "0"},
            },
            2: {
                1: {"question": "E1PBS2 What is 1 - 2?", "options": ["-1", "-2", "0"], "answer": "-1"},
                2: {"question": "E1PBS2 What is 1 - 3?", "options": ["-3", "-2", "-1"], "answer": "-2"},
            }
        }
    },
    2: {
        "A": {
            1: {
                1: {"question": "E2PAS1 What is 2 + 1?", "options": ["2", "3", "4"], "answer": "3"},
                2: {"question": "E2PAS1 What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
            },
            2: {
                1: {"question": "E2PAS2 What is 2 + 3?", "options": ["4", "5", "6"], "answer": "5"},
                2: {"question": "E2PAS2 What is 2 + 4?", "options": ["5", "6", "7"], "answer": "6"},
            }
        },
        "B": {
            1: {
                1: {"question": "E2PBS1 What is 2 - 1?", "options": ["0", "1", "2"], "answer": "1"},
                2: {"question": "E2PBS1 What is 2 - 2?", "options": ["0", "1", "2"], "answer": "0"},
            },
            2: {
                1: {"question": "E2PBS2 What is 2 - 3?", "options": ["-2", "-1", "0"], "answer": "-1"},
                2: {"question": "E2PBS2 What is 2 - 4?", "options": ["-3", "-2", "-1"], "answer": "-2"},
            }
        }
    },
    3: {
        "A": {
            1: {
                1: {"question": "E3PAS1 What is 3 + 1?", "options": ["3", "4", "5"], "answer": "4"},
                2: {"question": "E3PAS1 What is 3 + 2?", "options": ["4", "5", "6"], "answer": "5"},
            },
            2: {
                1: {"question": "E3PAS2 What is 3 + 3?", "options": ["5", "6", "7"], "answer": "6"},
                2: {"question": "E3PAS2 What is 3 + 4?", "options": ["6", "7", "8"], "answer": "7"},
            }
        },
        "B": {
            1: {
                1: {"question": "E3PBS1 What is 3 - 1?", "options": ["1", "2", "3"], "answer": "2"},
                2: {"question": "E3PBS1 What is 3 - 2?", "options": ["0", "1", "2"], "answer": "1"},
            },
            2: {
                1: {"question": "E3PBS2 What is 3 - 3?", "options": ["0", "1", "2"], "answer": "0"},
                2: {"question": "E3PBS2 What is 3 - 4?", "options": ["-1", "0", "1"], "answer": "-1"},
            }
        }
    },
    4: {
        "A": {
            1: {
                1: {"question": "E4PAS1 What is 4 + 1?", "options": ["4", "5", "6"], "answer": "5"},
                2: {"question": "E4PAS1 What is 4 + 2?", "options": ["5", "6", "7"], "answer": "6"},
            },
            2: {
                1: {"question": "E4PAS2 What is 4 + 3?", "options": ["6", "7", "8"], "answer": "7"},
                2: {"question": "E4PAS2 What is 4 + 4?", "options": ["7", "8", "9"], "answer": "8"},
            }
        },
        "B": {
            1: {
                1: {"question": "E4PBS1 What is 4 - 1?", "options": ["2", "3", "4"], "answer": "3"},
                2: {"question": "E4PBS1 What is 4 - 2?", "options": ["1", "2", "3"], "answer": "2"},
            },
            2: {
                1: {"question": "E4PBS2 What is 4 - 3?", "options": ["0", "1", "2"], "answer": "1"},
                2: {"question": "E4PBS2 What is 4 - 4?", "options": ["0", "1", "2"], "answer": "0"},
            }
        }
    },
    5: {
        "A": {
            1: {
                1: {"question": "E5PAS1 What is 5 + 1?", "options": ["5", "6", "7"], "answer": "6"},
                2: {"question": "E5PAS1 What is 5 + 2?", "options": ["6", "7", "8"], "answer": "7"},
            },
            2: {
                1: {"question": "E5PAS2 What is 5 + 3?", "options": ["7", "8", "9"], "answer": "8"},
                2: {"question": "E5PAS2 What is 5 + 4?", "options": ["8", "9", "10"], "answer": "9"},
            }
        },
        "B": {
            1: {
                1: {"question": "E5PBS1 What is 5 - 1?", "options": ["3", "4", "5"], "answer": "4"},
                2: {"question": "E5PBS1 What is 5 - 2?", "options": ["2", "3", "4"], "answer": "3"},
            },
            2: {
                1: {"question": "E5PBS2 What is 5 - 3?", "options": ["1", "2", "3"], "answer": "2"},
                2: {"question": "E5PBS2 What is 5 - 4?", "options": ["0", "1", "2"], "answer": "1"},
            }
        }
    }
}


USED_STAGE_QUESTIONS = {
    stage_id: ALL_STAGE_QUESTIONS[stage_id]
    for stage_id in sorted(ALL_STAGE_QUESTIONS.keys())[:MAX_STAGES]
}

async def get_stage_data(context=None, stage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    stage_data = USED_STAGE_QUESTIONS[stage]
    return stage_data

async def get_substage_data(context=None, stage=None, substage=None):
    if substage is None:
        substage = context.chat_data["current_substage"]
    
    stage_data = await get_stage_data(context, stage)
    substage_data = stage_data.get(substage)
    return substage_data

async def get_subset_data(context=None, stage=None, substage=None, subset=None):
    if subset is None:
        subset = context.chat_data["current_subset"]

    substage_data = await get_substage_data(context, stage, substage)
    subset_data = substage_data.get(subset)

    return subset_data

async def get_question_data(question_id, context=None, stage=None, substage=None, subset=None):
    if subset is None:
        subset = context.chat_data["current_subset"]

    subset_data = await get_subset_data(context, stage, substage)
    question_data = subset_data.get(question_id)
    return question_data

#endregion

#region CURRENT SUBSETS

CURRENT_SUBSTAGE_SET = {
    1: {
        "A": 1,
        "B": 1
    },
    2: {
        "A": 1,
        "B": 1
    },
    3: {
        "A": 1,
        "B": 1
    },
    4: {
        "A": 1,
        "B": 1
    },
    5: {
        "A": 1,
        "B": 1
    }
}

subset_lock = asyncio.Lock()

async def get_and_switch_subset(context=None, stage=None, substage=None):
    subset = await get_subset(context, stage, substage)
    await switch_subset(context, stage, substage)

    return subset

async def get_subset(context=None, stage=None, substage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    if substage is None:
        substage = context.chat_data["current_substage"]

    async with subset_lock:
        subset = CURRENT_SUBSTAGE_SET[stage][substage]

    return subset

async def switch_subset(context=None, stage=None, substage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    if substage is None:
        substage = context.chat_data["current_substage"]

    async with subset_lock:

        if CURRENT_SUBSTAGE_SET[stage][substage] == 1:
            CURRENT_SUBSTAGE_SET[stage][substage] = 2

        elif CURRENT_SUBSTAGE_SET[stage][substage] == 2:
            CURRENT_SUBSTAGE_SET[stage][substage] = 1

#endregion

#region CURRENT STAGES

ACTIVE_STAGES = {
    stage_id: {"total": 0, "A": 0, "B": 0}
    for stage_id in USED_STAGE_QUESTIONS.keys()
}

active_stages_lock = asyncio.Lock()

async def get_smallest_stage(context):
    completed_stages = context.chat_data["completed_stages"]

    async with active_stages_lock:
        suitable_stages = [
            (stage_id, data["total"])
            for stage_id, data in ACTIVE_STAGES.items()
            if stage_id not in completed_stages
        ]
        
        if not suitable_stages:
            raise ValueError("No suitable stages available")

        smallest_stage, users = min(suitable_stages, key = lambda x: x[1])

        return smallest_stage

async def update_add_stage_users(context=None, stage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    async with active_stages_lock:

        ACTIVE_STAGES[stage]["total"] += 1

    
async def update_remove_stage_users(context=None, stage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    async with active_stages_lock:

        ACTIVE_STAGES[stage]["total"] -= 1

async def get_next_substage(context):
    completed_substages = context.chat_data["completed_substages"]

    if completed_substages == []:
        next_substage = await get_smallest_substage(context)

    elif completed_substages == ["A"]:
        next_substage = "B"

    elif completed_substages == ["B"]:
        next_substage = "A"

    return next_substage

async def get_smallest_substage(context=None, stage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    async with active_stages_lock:

        A_users = ACTIVE_STAGES[stage]["A"]
        B_users = ACTIVE_STAGES[stage]["B"]
    
    if A_users >= B_users:
        return "B"
    
    elif B_users > A_users:
        return "A"
    
async def update_add_substage_users(context=None, stage=None, substage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]
    if substage is None:
        substage = context.chat_data["current_substage"]

    async with active_stages_lock:
        ACTIVE_STAGES[stage][substage] += 1

async def update_remove_substage_users(context=None, stage=None, substage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]
    if substage is None:
        substage = context.chat_data["current_substage"]

    async with active_stages_lock:
        ACTIVE_STAGES[stage][substage] -= 1

#region STAGE ORDER

#endregion
        
#endregion

#endregion

#region IMAGE INTERFACE

IMAGE_FOLDER = "test_images"

STAGE_IMAGES = {
    1: "stage 1.png", 
    2: "stage 2.jpg", 
    3: "stage 3.png", 
    4: "stage 4.jpg", 
    5: "stage 5.jpg", 
    6: "stage 6.jpg",  
    7 : "stage 7.jpg",
}

async def is_image_in_stage(context=None, stage=None):
    if stage is None:
        stage = context.chat_data["current_stage"]

    image = STAGE_IMAGES.get(stage)

    return image is not None

async def get_stage_image_file(context=None, stage=None):
    await asyncio.sleep(0.1)

    if stage is None:
        stage = context.chat_data["current_stage"]

    image_filename = STAGE_IMAGES.get(stage)
    image_folder = os.path.join(os.path.dirname(__file__), IMAGE_FOLDER)
    image_path = os.path.join(image_folder, image_filename)
    image_file = open(image_path, 'rb')

    return image_file

#endregion

#region QUIZ INTERFACE

async def initialise_quiz_values(context, update=Update):
    chat_id = str(update.effective_chat.id)

    context.chat_data["started"] = True
    context.chat_data["chat_id"] = chat_id
    context.chat_data["group_number"] = await get_group_number(chat_id=chat_id)
    context.chat_data["completed_stages"] = []
    context.chat_data["score"] = 0

    context.chat_data["current_stage"] = None
    context.chat_data["completed_substages"] = []

    context.chat_data["current_substage"] = None
    context.chat_data["current_subset"] = None
    context.chat_data["answered_questions"] = []

async def update_quiz_values(context):
    current_stage = context.chat_data["current_stage"]
    context.chat_data["completed_stages"].append(current_stage)

async def is_quiz_complete(context):
    completed_stages = context.chat_data["completed_stages"]
    total_stages = USED_STAGE_QUESTIONS

    return len(completed_stages) >= len(total_stages)

async def initialise_stage_values(context, stage):
    context.chat_data["current_stage"] = stage
    context.chat_data["completed_substages"] = []

async def update_stage_values(context):
    substage = context.chat_data["current_substage"]
    context.chat_data["completed_substages"].append(substage)

async def is_stage_complete(context):
    completed_substages = context.chat_data["completed_substages"]
    total_substages = await get_stage_data(context)

    return len(completed_substages) >= len(total_substages)

async def initialise_substage_values(context, substage, subset):
    stage = context.chat_data["current_stage"]
    
    context.chat_data["current_substage"] = substage
    context.chat_data["current_subset"] = subset
    context.chat_data["answered_questions"] = []
    context.chat_data["currently_answered"] = []

async def update_substage_values_correct(context, question_id):
    context.chat_data["answered_questions"].append(question_id)
    context.chat_data["score"] += CORRECT_SCORE
    if question_id in context.chat_data["currently_answered"]:
        context.chat_data["currently_answered"].remove(question_id)

async def update_substage_values_wrong(context):
    context.chat_data["score"] += WRONG_SCORE

async def is_substage_complete(context):
    answered_questions = context.chat_data["answered_questions"]
    subset_questions = await get_subset_data(context)

    return len(answered_questions) >= len(subset_questions)

#endregion

#endregion

#region ONBOARDING

async def start_command(update=Update, context=ContextTypes.DEFAULT_TYPE):
    async with onboarding_semaphore:
        if await is_chat_private(update):

            if await is_not_yet_ready(context):
                await ask_are_you_ready(update, context)

            else:
                await send_onboard_instructions(update, context)

        else:
            await send_help(update, context)

async def handle_ready(update, query, button_data, context):
    context.user_data["ready"] = True

    new_text = f"Welcome! 😁\n\nAre you ready to begin the quiz?"
    await safe_send(query.edit_message_text, text=new_text)

    await set_group_number(context)
    await send_onboard_instructions(update, context)

#region ONBOARDING BEHAVIOUR

async def is_chat_private(update):
    chat_type = update.effective_chat.type

    return chat_type == "private"

async def is_not_yet_ready(context):
    ready = context.user_data.get("ready", None)

    return ready is not True

async def ask_are_you_ready(update, context):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    yes_button = InlineKeyboardButton("yes", callback_data="ready")
    keyboard = InlineKeyboardMarkup([[yes_button]])
    text = "Welcome! 😁\n\nAre you ready to begin the quiz?"

    await safe_send(context.bot.send_message, chat_id, text, reply_markup=keyboard, reply_to_message_id=message_id)

async def send_onboard_instructions(update, context):
    chat_id = update.effective_chat.id
    group_number = context.user_data["group_number"]
    group_link = await get_group_link(context)

    text = f"You are in group {group_number}! \n\n1. Join the group using the link: \n{group_link} \n\n2. Wait for everyone else to join \n\n3. Start the quiz by sending /quiz"

    await safe_send(context.bot.send_message, chat_id, text)

async def send_help(update, context):
    return False

#endregion

#endregion

#region QUIZ

#region START QUIZ

async def start_quiz_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if not await is_chat_private(update):

        if context.chat_data.get("started") != True:
            
            if LOAD_SAVE_FILE != True:
                await start_quiz(update, context)

            elif LOAD_SAVE_FILE == True:
                await resume_quiz(update, context)

        else:
            load_state()
            await resume_quiz(update, context)

    else:
        await send_onboard_instructions(update, context)

async def start_quiz(update, context):
    chat_id = str(update.effective_chat.id)
    async with chat_locks[chat_id]:
       await initialise_quiz_values(context, update)

       group_number = context.chat_data["group_number"]
       print(f"Group {group_number} started quiz")
       await send_starting_quiz(context)

    await start_next_stage(context)

async def resume_quiz(update, context):
    chat_id = str(update.effective_chat.id)
    async with chat_locks[chat_id]:
        await initialise_saved_quiz_values(update, context)
        
        if await is_quiz_complete(context):
            await send_quiz_complete(context)

        else:
            await send_resuming_stage(context)
            await print_resuming_quiz(context)
    
    await ask_next_subset_questions(context)


#region START QUIZ BEHAVIOUR

async def send_starting_quiz(context):
    chat_id = context.chat_data["chat_id"]

    text = "Starting quiz..."
    await safe_send(context.bot.send_message, chat_id, text)

#endregion
    

#region CONTINUE QUIZ BEHAVIOUR

async def initialise_saved_quiz_values(update, context):
    chat_id = str(update.effective_chat.id)
    group_number = await get_group_number(chat_id=chat_id)
    group_data = await get_group_data(group_number=group_number)

    context.chat_data["started"] = True
    context.chat_data["chat_id"] = chat_id
    context.chat_data["group_number"] = group_number
    context.chat_data["current_stage"] = group_data.get("current_stage")
    context.chat_data["completed_stages"] = group_data.get("completed_stages")
    context.chat_data["score"] = group_data.get("score")
    context.chat_data["current_substage"] = group_data.get("current_substage")
    context.chat_data["completed_substages"] = group_data.get("completed_substages")
    context.chat_data["current_subset"] = group_data.get("current_subset")
    context.chat_data["answered_questions"] = group_data.get("answered_questions")
    context.chat_data["currently_answered"] = []

async def send_resuming_stage(context):
    chat_id = context.chat_data["chat_id"]
    stage = context.chat_data["current_stage"]

    text = f"Resuming stage {stage}..."
    
    if await is_image_in_stage(context):
        image_file = await get_stage_image_file(context)
        await safe_send(context.bot.send_photo, chat_id, photo=image_file, caption=text)

    else:
        await safe_send(context.bot.send_message, chat_id, text)

async def print_resuming_quiz(context):
    group = context.chat_data["group_number"]
    stage = context.chat_data["current_stage"]
    part = context.chat_data["current_substage"]
    subset = context.chat_data["current_subset"]

    print(f"Group {group} resuming part {part} of stage {stage} (Subset {subset})")

#endregion

#endregion

#region STAGE SYSTEM

async def end_stage(context):
    chat_id = context.chat_data["chat_id"]
    async with chat_locks[chat_id]:
        await update_quiz_values(context)
        await print_stage_complete(context)
        await send_stage_complete(context)
        await update_remove_stage_users(context)
        await update_stage_status_remove(context)
        await update_group_status(context)
        await asyncio.sleep(0.3)

    if await is_quiz_complete(context):
        await send_quiz_complete(context)
        await print_quiz_complete(context)

    else:
        await start_next_stage(context)

#region END STAGE BEHAVIOUR

async def send_quiz_complete(context):
    chat_id = context.chat_data["chat_id"]
    score = context.chat_data["score"]

    text=f"Congratulations!🎉 \n\nYou have completed the quiz! 🥳"
    await safe_send(context.bot.send_message, chat_id, text)

async def print_quiz_complete(context):
    group_number = context.chat_data["group_number"]

    print(f"Group {group_number} finished quiz")

async def send_stage_complete(context):
    stage = context.chat_data["current_stage"]
    score = context.chat_data["score"]
    chat_id = context.chat_data["chat_id"]

    text = f"✅ Stage {stage} complete! ✅\n\nCurrent score: {score}"
    await safe_send(context.bot.send_message, chat_id, text)

async def print_stage_complete(context):
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    print(f"Group {group} completed stage {stage}")

#endregion

async def start_next_stage(context):
    chat_id = context.chat_data["chat_id"]
    async with chat_locks[chat_id]:
        try:
            next_stage = await get_smallest_stage(context)
        except Exception as e:
            return
    
        await initialise_stage_values(context, next_stage)
        await update_add_stage_users(context)
        await print_starting_stage(context)
        await update_stage_status_add(context)
        await update_group_status(context)
        await send_starting_stage(context)
    
    await start_next_substage(context)

#region START STAGE BEHAVIOUR

async def send_starting_stage(context):
    chat_id = context.chat_data["chat_id"]
    stage = context.chat_data["current_stage"]

    text = f"Starting stage {stage}..."

    if await is_image_in_stage(context):
        image_file = await get_stage_image_file(context)
        await safe_send(context.bot.send_photo, chat_id, photo=image_file, caption=text)

    else:
        await safe_send(context.bot.send_message, chat_id, text)

async def print_starting_stage(context):
    group_number = context.chat_data["group_number"]
    stage = context.chat_data["current_stage"]

    print(f"Group {group_number} started stage {stage}")

#endregion

#endregion

#region SUBSTAGE SYSTEM

async def end_substage(context):
    chat_id = context.chat_data["chat_id"]
    async with chat_locks[chat_id]:
        await update_stage_values(context)
        await print_substage_complete(context)
        await update_remove_substage_users(context)

    if await is_stage_complete(context):
        await end_stage(context)

    else:
        await start_next_substage(context)

#region END SUBSTAGE BEHAVIOUR

async def print_substage_complete(context):
    group_number = context.chat_data["group_number"]
    current_stage = context.chat_data["current_stage"]
    current_substage = context.chat_data["current_substage"]
    subset = context.chat_data["current_subset"]

    print(f"Group {group_number} completed part {current_substage} of stage {current_stage} (Subset {subset})")

#endregion

async def start_next_substage(context):
    chat_id = context.chat_data["chat_id"]
    async with chat_locks[chat_id]:
        next_substage = await get_next_substage(context)
        subset = await get_and_switch_subset(context, substage=next_substage)

        await initialise_substage_values(context, next_substage, subset)
        await update_add_substage_users(context)
        await update_group_status(context)
        await print_starting_substage(context)
    
    await ask_next_subset_questions(context)

#region START SUBSTAGE BEHAVIOUR

async def print_starting_substage(context):
    group = context.chat_data["group_number"]
    stage = context.chat_data["current_stage"]
    substage = context.chat_data["current_substage"]
    subset = context.chat_data["current_subset"]

    print(f"Group {group} started part {substage} of stage {stage} (Subset {subset})")

#endregion

#endregion

#region QUESTION SYSTEM

async def ask_next_subset_questions(context):
    chat_id = context.chat_data["chat_id"]
    total_answered = len(context.chat_data["answered_questions"])
    total_questions = len(await get_subset_data(context))
    total_currently = len(context.chat_data["currently_answered"])
    remaining_questions = total_questions - total_answered - total_currently

    if total_answered == total_questions:
        await end_substage(context)

    elif remaining_questions == 0:
        pass

    elif QUESTION_SEQUENCING_MODE == "1b1":
        if remaining_questions > 0:
            async with chat_locks[chat_id]:
                await ask_question(context, total_answered+1)
                context.chat_data["currently_answered"].append(total_answered+1)

    elif QUESTION_SEQUENCING_MODE == "2b2":
        if remaining_questions >= 2 and total_currently == 0:
            async with chat_locks[chat_id]:
                next_question = await get_next_question_id(context)
                await ask_question(context, next_question)
                context.chat_data["currently_answered"].append(next_question)

            async with chat_locks[chat_id]:
                next_question = await get_next_question_id(context)
                await ask_question(context, next_question)
                context.chat_data["currently_answered"].append(next_question)

        elif total_currently <= 1 and remaining_questions == 1:
            async with chat_locks[chat_id]:
                next_question = await get_next_question_id(context)
                await ask_question(context, next_question)
                context.chat_data["currently_answered"].append(next_question)

async def get_next_question_id(context):
    answered = context.chat_data["answered_questions"]
    currently = context.chat_data["currently_answered"]
    used = answered + currently
    substage_data = await get_substage_data(context)
    all_questions = substage_data.keys()

    for question in all_questions:
        if question not in used:
            return question

async def ask_question(context, question_id):
    await asyncio.sleep(0.3)
    question_data = await get_question_data(question_id, context)
    question = question_data["question"]
    options = question_data["options"]
    chat_id = context.chat_data["chat_id"]

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text= option, callback_data= f"quiz:{question_id}:{option}")]
        for option in options
    ]) 
    text = question
    await safe_send(context.bot.send_message, chat_id, text, reply_markup=keyboard) 

async def handle_question(update, query, response_data, context):
    chat_id = str(update.effective_chat.id)
    async with chat_locks[chat_id]:
        async with question_send_semaphore:
            await asyncio.sleep(0.1)

            prefix, question_id, selected = response_data.split(":")
            question_id = int(question_id)
            question_data = await get_question_data(question_id, context)
            question = question_data["question"]
            answer = question_data["answer"]

            if question_id not in context.chat_data["answered_questions"] and question_id in context.chat_data["currently_answered"]:

                if selected == answer:
                    await update_substage_values_correct(context, question_id)
                    await send_answer_correct(query, context, question ,selected)
                    await update_group_status(context)
                    
                elif selected != answer:
                    await update_substage_values_wrong(context)
                    await send_answer_wrong(query, context, question ,selected)

    if selected == answer:
        await ask_next_subset_questions(context)

#region HANDLE QUESTION BEHAVIOUR

async def send_answer_correct(query, context, question, selected):
    score = context.chat_data["score"]
    chat_id = context.chat_data["chat_id"]

    new_text = f"{question} \n\nYou selected: {selected} ✅\n Score: {score}"
    await safe_send(query.edit_message_text, text=new_text)

async def send_answer_wrong(query, context, question ,selected):
    score = context.chat_data["score"]

    old_keyboard = query.message.reply_markup.inline_keyboard
    new_keyboard = InlineKeyboardMarkup([
        [button] for row in old_keyboard for button in row if button.text != selected
    ])
    new_text = f"{question} \n\nYou selected {selected} ❌ \nTry again! \nScore: {score}"

    await safe_send(query.edit_message_text, text=new_text, reply_markup=new_keyboard)

#endregion

#endregion

#endregion

#region ADMIN MODULE

#region GROUP CHAT DATA

NEED_UPDATING = False

stage_status_lock = asyncio.Lock()
group_status_lock = asyncio.Lock()

GROUP_STATUS = {
        group_number: {"current_stage": None, 
                       "completed_stages": [], 
                       "score": 0, 
                       "current_substage" : None,
                       "completed_substages": [],
                       "current_subset": None, 
                       "answered_questions": []
                       }
                       for group_number in range(1, MAX_GROUPS+1)
                }

STAGE_STATUS = {
        stage_number: set()
        for stage_number in range(1, MAX_STAGES+1)
    }


async def update_stage_status_add(context):
    global NEED_UPDATING
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    async with stage_status_lock:
        STAGE_STATUS[stage].add(group)
        NEED_UPDATING = True

    await save_state()


async def update_stage_status_remove(context):
    global NEED_UPDATING
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    async with stage_status_lock:
        STAGE_STATUS[stage].discard(group)
        NEED_UPDATING = True

    await save_state()


async def update_group_status(context):
    global NEED_UPDATING
    stage = context.chat_data["current_stage"]
    completed_stages = context.chat_data["completed_stages"]
    group = context.chat_data["group_number"]
    score = context.chat_data["score"]
    substage = context.chat_data["current_substage"]
    completed_substages = context.chat_data["completed_substages"]
    subset = context.chat_data["current_subset"]
    answered = context.chat_data["answered_questions"]

    async with group_status_lock:
        if not await is_quiz_complete(context):
            GROUP_STATUS[group]["current_stage"] = stage
            GROUP_STATUS[group]["completed_stages"] = completed_stages
            GROUP_STATUS[group]["score"] = score
            GROUP_STATUS[group]["current_substage"] = substage
            GROUP_STATUS[group]["completed_substages"] = completed_substages
            GROUP_STATUS[group]["current_subset"] = subset
            GROUP_STATUS[group]["answered_questions"] = answered

        else:
            GROUP_STATUS[group] = f"Completed quiz. Score: {score}"

        NEED_UPDATING = True
        await save_state()

#endregion

#region GROUP TRACKER

ADMIN_DASHBOARD_MESSAGE_ID = None

async def update_dashboard(application):
    global ADMIN_DASHBOARD_MESSAGE_ID
    
    try:
        stage_lines = ["🧱 <b>Stage Overview</b> 🧱"]
        async with stage_status_lock:
            for stage in range(1, MAX_STAGES+1):
                groups = sorted(STAGE_STATUS[stage])
                stage_line = f"Stage {stage} → Groups:  {','.join(map(str, groups)) if groups else '-'}"
                stage_lines.append(stage_line)

        group_lines = ["\n👥 <b>Group Status</b> 👥"]
        async with group_status_lock:
            for group in range(1, MAX_GROUPS+1):
                status = GROUP_STATUS[group]
                if isinstance(status, str):
                    group_lines.append(f"Group {group} → {status}")
                else:
                    stage = status["current_stage"]
                    score = status["score"]
                    completed = len(status["completed_stages"])
                    group_lines.append(f"\nGroup {group}: \nStage → {stage} \nScore → {score} \nCompleted → {completed}/{MAX_STAGES}")

        dashboard_text = "\n".join(stage_lines + group_lines)

        if ADMIN_DASHBOARD_MESSAGE_ID:
            await safe_send(application.bot.edit_message_text,
                            chat_id=ADMIN_CHAT_ID,
                            message_id=ADMIN_DASHBOARD_MESSAGE_ID,
                            text=dashboard_text,
                            parse_mode="HTML")
        else:
            msg = await safe_send(application.bot.send_message,
                                  chat_id=ADMIN_CHAT_ID,
                                  text=dashboard_text,
                                  parse_mode="HTML")
            ADMIN_DASHBOARD_MESSAGE_ID = msg.message_id

    except Exception as e:
        print(f"❌ Dashboard update error: {e}")

async def dashboard_job_callback(context: ContextTypes.DEFAULT_TYPE):
    global NEED_UPDATING
    if NEED_UPDATING == True:
        await update_dashboard(context.application)
        NEED_UPDATING = False

#endregion

#region BROADCAST

async def broadcast_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id == ADMIN_CHAT_ID:
        None

        if not context.args:
            await update.message.reply_text("Usage: /broadcast Your message here")

        else:
            message = " ".join(context.args)
            print(f"Broadcasting: {message}")
            success = 0
            failed = 0

            for chat_id in ALL_CHAT_IDS:

                try:
                    await safe_send(context.bot.send_message, chat_id=chat_id, text=message)
                    success += 1

                except Exception as e:
                    print(f"❌ Failed to send to {chat_id}: {e}")
                    failed += 1

            if success == MAX_GROUPS:
                await update.message.reply_text(f"✅ Sent to every chat")

            else:
                await update.message.reply_text(f"✅ Sent to {success} chats. ❌ Failed: {failed}")

            



#endregion

#endregion

#region SAVE FILE

async def save_state():
    global GROUP_STATUS, STAGE_STATUS

    try:
        data = {
            "GROUP_STATUS": GROUP_STATUS,
            "STAGE_STATUS": {k: list(v) for k, v in STAGE_STATUS.items()}
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"❌ Failed to save quiz state: {e}")

def load_state():
    global GROUP_STATUS, STAGE_STATUS
    
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)

            loaded_group_status = data.get("GROUP_STATUS", {})
            GROUP_STATUS = {int(k): v for k, v in loaded_group_status.items()}
            
            loaded_stage_status = data.get("STAGE_STATUS", {})
            STAGE_STATUS = {int(k): set(v) for k, v in loaded_stage_status.items()}

            print("✅ Quiz state loaded from file.")
        except Exception as e:
            print(f"❌ Failed to load quiz state: {e}")

async def reset_state():
    global GROUP_STATUS, STAGE_STATUS

    GROUP_STATUS = {
        group_number: {"current_stage": None, 
                       "completed_stages": [], 
                       "score": 0, 
                       "current_substage" : None,
                       "completed_substages": [],
                       "current_subset": None, 
                       "answered_questions": []
                       }
                       for group_number in range(1, MAX_GROUPS+1)
                }

    STAGE_STATUS = {
        stage_number: set()
        for stage_number in range(1, MAX_STAGES+1)
    }

    await save_state()

async def get_group_data(context=None, group_number=None):
    if group_number is None:
        group_number = context.chat_data["group_number"]

    group_data = GROUP_STATUS.get(group_number)
    return group_data



#region BUTTON HANDLER

handlers = {
        "ready": handle_ready,
        "quiz": handle_question
    }

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    button_data = query.data
    prefix = button_data.split(":")[0] if ":" in button_data else button_data
    handler = handlers.get(prefix)

    if handler:
        await handler(update, query, button_data, context)
    else:
        await safe_send(query.edit_message_text, "Unknown button pressed.")

#endregion

#region RUN BOT

if __name__ == "__main__":
    job_queue = JobQueue()

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .defaults(defaults)
        .rate_limiter(AIORateLimiter())
        .concurrent_updates(200)
        .request(request)
        .job_queue(job_queue)  # ✅ Proper way to enable job queue
        .build()
    )


    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("quiz", start_quiz_command))
    app.add_handler((CommandHandler("broadcast", broadcast_command)))

    app.add_handler(CallbackQueryHandler(handle_button))

    app.job_queue.run_repeating(
    dashboard_job_callback,
    interval=10,      
    first=5,
    job_kwargs={"max_instances": 1}           
)

    print("✅ Polling 9...")
    
    if LOAD_SAVE_FILE == True:
        load_state()

    app.run_polling()

#endregion