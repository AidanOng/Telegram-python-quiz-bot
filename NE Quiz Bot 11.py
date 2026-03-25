#region CUSTOMISATION

TOKEN = "7825229101:AAE05RuZmVEhIGXNdTQh_IYwA6i3--RMwWc"
#Test bot: 7511843239:AAGnd7fcEYmrhWqs1MnvD3EKm41VXK2YuI4
# Real bot: 7825229101:AAE05RuZmVEhIGXNdTQh_IYwA6i3--RMwWc

SEND_IMAGES = False
IMAGE_FOLDER = "event_images"

SAVE_FILE = "quiz_state.json"
LOAD_SAVE_FILE = False   
RESET_SAVE_FILE = False

GROUP_ALLOCATION = ["random", "in_order", "fill_up", "custom"]
GROUP_ALLOCATION_MODE = GROUP_ALLOCATION[1]

STAGE_ALLOCATION = ["predefined", "dynamic"]
STAGE_ALLOCATION_MODE = STAGE_ALLOCATION[1]

QUESTION_SEQUENCING = ["1b1", "2b2"]
QUESTION_SEQUENCING_MODE = QUESTION_SEQUENCING[0]

LOG_MESSAGES = False
MESSAGE_LOG_FILE = None

SCORE_UPDATING = ["static", "dynamic"]
SCORE_UPDATING_MODE = SCORE_UPDATING[1]
CORRECT_SCORE = 30
WRONG_SCORE = -10

MAX_STAGES = 5

MAX_GROUPS = 7
MAX_PER_GROUP = 10

ADMIN_CHAT_ID = -1002835681583

#region CUSTOM DATA

GROUP_CHAT_IDS_NUMBERS = {
    "-1002821470426" : 1,
    "-1002872717963" : 2,
    "-1002737488073" : 3,
    "-1002522472377" : 4,
    "-1002810991483" : 5,
    "-1002679223221" : 6,
    "-1002696767672" : 7
}

GROUP_LINKS = {
    1: "https://t.me/+S3zxt1jmfStjNmU1",
    2: "https://t.me/+Fjsz1QchQAtlMjM1",
    3: "https://t.me/+bToLiWHt--wxMTc1",
    4: "https://t.me/+cAHxW34NWeJlYTM1",
    5: "https://t.me/+81FBcn2aJthkZDg1",
    6: "https://t.me/+jSVX4yf7cK42MDBl",
    7: "https://t.me/+hmKg-OFnoHw2ODI1"
}

OPTIONS = ["A", "B", "C", "D"]
ALL_STAGE_QUESTIONS = {
    1: {
        "A": {
            1: {
                1: {"question": "A1 What region is depicted in Ptolemy's Eleventh Map of Asia?\n\nA. Southeast Asia\nB. Northeast Asia\nC. Southwest Asia\nD. Northwest Asia", "answer": "A", "image": "1A1.jpeg"},
                2: {"question": "A2 Who offered Singapore as a gift to Alexander Hamilton in 1703?\n\nA. Sultan Abdul Jalil IV of Johor\nB. Alexander Hamilton himself\nC. The Scottish government\nD. The East India Company", "answer": "A", "image": "1A21A5.jpeg"},
                3: {"question": "A3 Who collected the prehistoric stone tools from Pulau Ubin, Singapore?\n\nA. Major P.D.R. Williams-Hunt, a prominent figure in the field of archaeology and an influential contributor to Singapore's historical research.\nB. Acting-Director of Museums for the Federation of Malaya, a key role in overseeing the curation and preservation of regional artifacts and heritage.\nC. A local archaeologist, actively involved in the excavation and study of Southeast Asia's rich historical sites.\nD. A group of students, engaging in fieldwork and academic research as part of their educational journey.", "answer": "A", "image": "1A3.jpeg"},
                4: {"question": "A4 Why does the map not place Singapura at the southernmost tip of the Malay Peninsula?\n\nA. Because it was not located within the Malay Peninsula.\nB. Because the cartographer made an error.\nC. Because the map is not drawn to scale.\nD. Because the location of Singapura was not well-known at that time.", "answer": "D", "image": "1A41B11B2.jpeg"},
                5: {"question": "A5 What were the advantages of Singapore's location, according to Alexander Hamilton?\n\nA. It was close to Europe\nB. It had good rivers and safe harbors\nC. It was near from other trade centers\nD. It had a large population", "answer": "B", "image": "1A21A5.jpeg"}
            }
        },
        "B": {
            1: {
                1: {"question": "B1 What is the name given to the southern tip of the Malay peninsula on the Sumatra and Malay Peninsula map?\n\nA. Senasur\nB. Singapore\nC. Nieuwe Straet\nD. Malay Peninsula", "answer": "A", "image": "1A41B11B2.jpeg"},
                2: {"question": "B2 What is the name given to the strait between the Malay peninsula and Sumatra on the map?\n\nA. Singapore Strait\nB. Nieuwe Straet (or New Strait)\nC. Strait of Malacca\nD. Java Sea", "answer": "B", "image": "1A41B11B2.jpeg"},
                3: {"question": "B3 What is the significance of the Mao Kun map in Chinese cartography?\n\nA. It's the earliest known map to depict the New World.\nB. It's the first map to show the sailing routes from China to Europe.\nC. It's the earliest known Chinese map to accurately depict Southern Asia, Persia, Arabia, and East Africa.\nD. It's a map of the Beijings dynasty's territorial conquests", "answer": "C", "image": "1B3.jpeg"},
                4: {"question": "B4 What is the name of the river mentioned in the description of Katib Celebi's map of Sumatra?\n\nA. Muar River\nB. Singapore River\nC. Johor River\nD. Pahang River", "answer": "A", "image": "1B4.jpeg"},
                5: {"question": "B5 How is Singapore island referred to in the 1794 chart of the East Indies?\n\nA. Singapura\nB. Sincapore\nC. Singa\nD. Singapore", "answer": "B", "image": "1B5.jpeg"}
            }
        }
    },
    2: {
        "A": {
            1: {
                1: {"question": "A1 What was the primary factor that led to the transformation of the Singapore River waterfront in the 1970s?\n\nA. Accelerated urban expansion coupled with a surge in population density\nB. Economic contraction and the erosion of longstanding industrial sectors\nC. State-driven initiatives in urban revitalization and systematic environmental remediation\nD. Escalating environmental challenges, including widespread pollution", "answer": "C"},
                2: {"question": "A2 What was the significance of travel trunks and chests for early immigrants to Singapore?\n\nA. They served as vessels for the preservation of food and water throughout the voyage.\nB. They often represented the sole tangible link to their homeland, cherished as mementos by immigrants.\nC. They were employed as carriers for essential tools and equipment vital to their labor.\nD. They functioned as secure containers for safeguarding critical documents.", "answer": "B"},
                3: {"question": "A3 What was the occasion for presenting the silver cup to William Farquhar?\n\nA. His formal designation as British Resident and Commandant of Singapore, marking a pivotal moment in the island's administration.\nB. His departure from Singapore in 1823, a significant turning point in the colonial narrative.\nC. His ascension to the rank of Lieutenant Colonel, reflecting his growing influence within the colonial military structure.\nD. His invaluable contribution to the William Farquhar Collection of Natural History Drawings, enhancing the documentation of Southeast Asia's biodiversity.", "answer": "B"},
                4: {"question": "A4 What was the primary mode of transportation for Chinese migrants traveling from Singapore to Hong Kong in the late 19th century?\n\nA. Steamship, revolutionizing maritime transport with its reliance on mechanized power.\nB. Junk, a traditional Chinese sailing vessel renowned for its distinctive design and pivotal role in regional trade.\nC. Sailboat, harnessing wind power for navigation across vast distances, a staple of maritime exploration.\nD. Ferry, facilitating the efficient transport of passengers and goods across short-distance waterways.", "answer": "B"},
                5: {"question": "A5 What was the significance of the Suez Canal's opening?\n\nA. It resulted in the enhanced frequency of mail packets, elevating their schedule to a monthly service.\nB. It transformed Singapore into a pivotal mail distribution hub, connecting Southeast Asia to distant global destinations and facilitating efficient communication.\nC. It introduced a system where mail could be collected and dispatched within a 24-hour window, streamlining postal operations.\nD. It marked the tradition of signaling the arrival of mail ships by hoisting a distinctive red flag atop Government Hill.", "answer": "B"}
            }
        },
        "B": {
            1: {
                1: {"question": "B1 Who drew the above art piece?\n\nA. Stephen Wiltshire\nB. Lee Sow Lim\nC. Katherine Kay-Mouat\nD. Ms Ng Chee Sun", "answer": "A", "image": "2B1.jpeg"},
                2: {"question": "B2 Who is the design firm responsible for the 88-meter-tall light sculpture in the Resorts World Sentosa waterfront development?\n\nA. Heatherwick Studio\nB. Benoy\nC. Pragma\nD. URA", "answer": "A"},
                3: {"question": "B3 What was the primary reason for the British imposing restrictions on rubber exports from the Federated Malay States in 1922?\n\nA. To safeguard environmental integrity and ensure sustainable practices within the industry.\nB. To assert dominance over the global rubber market, securing control of production and pricing dynamics.\nC. To shield the rubber industry from the detrimental effects of overproduction and the subsequent decline in market prices.\nD. To accelerate the transition towards synthetic rubber, reducing dependency on natural sources.", "answer": "C"},
                4: {"question": "B4 What was the main purpose of the Cantonese Rattan Industry Association formed in 1909?\n\nA. To advocate for the integration of rattan as a primary material in the furniture-making industry.\nB. To establish a robust export network, positioning rattan as a sought-after commodity in international markets.\nC. To consolidate power within the rattan processing sector, securing dominance over the industry in Singapore.\nD. To create sustainable employment pathways for local artisans, fostering craftsmanship and skill development.", "answer": "C"},
                5: {"question": "B5 What was the significance of Singapore in the rubber industry during the early 20th century?\n\nA. It held the title of the world's largest rubber producer, dominating global production.\nB. It functioned as a vital nexus, enabling rubber growers to connect with international agents and seamlessly distribute their goods worldwide.\nC. It emerged as the leading consumer of rubber across Southeast Asia, fueling regional demand.\nD. It served as the primary conduit for rubber exports to European markets, driving transcontinental trade.", "answer": "B"}
            }
        }
    },
    3: {
        "A": {
            1: {
                1: {"question": "A1 What was the original name of the Singapore Turf Club?\n\nA. Singapore Sporting Club\nB. Farrer Park Racing Club\nC. Singapore Horse club\nD. Singapore Horse Racing Union", "answer": "A"},
                2: {"question": "A2 What is the significance of the Chinese export silver mug displayed in the exhibit?\n\nA. It was used during royal banquets\nB. It was a souvenir presented by Chinese residents from the 1875 horse race\nC. It belonged to the British Governor\nD. It was a gift from the Chinese government", "answer": "B"},
                3: {"question": "A3 What was the significance of moving the Turf Club from Farrer Park in 1927?\n\nA. To reduce the influence of local communities\nB. To privatise the horse racing scene\nC. To relocate racing to a more accessible place\nD. To develop the land for public housing and urban improvement", "answer": "D"},
                4: {"question": "A4 What innovative method is described in relation to Pulau Tekong's land reclamation?\n\nA. Use of a polder system\nB. Floating construction platforms\nC. Dry earth moving equipments\nD. Use of geotextile for soil stabilisation", "answer": "A"},
                5: {"question": "A5 Why is Tuas Port considered significant to Singapore in the future?\n\nA. It supports only asia's cargo routes\nB. It is being redeveloped to be the world's largest container terminal in a single location\nC. It will be the most busiest port in the world\nD. It is Singapore's oldest trading hub", "answer": "B"}
            }
        },
        "B": {
            1: {
                1: {"question": "B1 What new material source is mentioned as part of Singapore's sustainable reclamation strategy?\n\nA. Landfill waste from pulau semakau\nB. Crushed bedrocks from the Singapore Straits\nC. construction and demolition waste from old buildings\nD. Trees from urban deforestation", "answer": "A"},
                2: {"question": "B2 What key transformation occurred on Pulau Bukom by 1970?\n\nA. Relocation of residents to mainland Singapore\nB. Development into a nature reserve\nC. Conversion into a naval base\nD. Extensive land reclamation for industrial use", "answer": "D"},
                3: {"question": "B3 What reclamation project was completed in 1953?\n\nA. Pulau Tekong\nB. Beach Road and Esplanade\nC. Marina Bay\nD. Tuas Port", "answer": "B"},
                4: {"question": "B4 What is the purpose of the mechanical tide gauge displayed in the exhibit?\n\nA. To track water pressure\nB. To monitor speed of water flow\nC. To measure water tides\nD. To measure rainfall", "answer": "C"},
                5: {"question": "B5 Complete the Sampan challenge and receive the code word from an NS admin Branch personnel!\n\nA. Lion\nB. Dog\nC. Cat\nD. Snake", "answer": "A"}
            }
        }
    },
    4: {
        "A": {
            1: {
                1: {"question": "A1 What year did Singapore's first volunteer fire brigade form?\n\nA. 1906 – A time of industrialization, but still early in the development of formalized emergency response services.\nB. 1888 – A period of significant growth for Singapore, yet volunteer fire services were still not fully organized.\nC. 1869 – The landmark year when Singapore's first volunteer fire brigade was formed, marking a major step in the city's urban safety evolution.\nD. 1948 – A post-war era focused on rebuilding, but the formation of fire brigades had already taken place much earlier.", "answer": "C"},
                2: {"question": "A2 According to The Malaya Tribune, what helped subdue the blaze?\n\nA. Modern fire engines – Technological advancements that made firefighting more efficient, though the early brigades operated with more basic equipment.\nB. Heavy rain – A factor influencing many aspects of Singapore's environment, but not a direct influence on the formation of the fire brigade.\nC. Co-operation between European and Asiatic members – A significant aspect of the volunteer brigade's success, where diverse communities worked together across racial and cultural lines to ensure the safety of the colony.\nD. Fireproof buildings – While fireproofing became a priority in later years, early efforts were more focused on training and organizing a functional fire brigade rather than building safety.", "answer": "C"},
                3: {"question": "A3 What were some of the major events that the SVC assisted in, and how did its contributions impact the outcome of these events?\n\nA. The SVC played a significant role in suppressing the Sepoy Mutiny of 1915 and defending strategic installations during the Japanese invasion of World War II.\nB. The SVC was integral to the training of local recruits between 1954 and 1956 under the National Service Ordinance, shaping the future of Singapore's military framework.\nC. The SVC contributed significantly to the defense efforts during the Konfrontasi in the 1960s, working alongside regional forces to address security threats.\nD. All of the above.", "answer": "D"},
                4: {"question": "A4 What was the significance of the swagger sticks in the Sikh Police Contingent?\n\nA. They symbolized the officer's rank and position within the corps, reflecting their level of authority and responsibility.\nB. They were used solely for ceremonial purposes, serving as a visual mark of formality rather than function.\nC. They were a mandatory part of the uniform, required for all officers regardless of their role or function.\nD. They were intended for self-defence, allowing officers to defend themselves in emergency situations.", "answer": "A"},
                5: {"question": "A5 What was the purpose of establishing the People's Defence Force (PDF) in Singapore?\n\nA. To provide a supplementary force to support the regular army, bolstering defense efforts during critical periods.\nB. To control rising crime rates and secret society influence, aiding the police in maintaining public order.\nC. To assist with transporting prisoners between Singapore and other countries, ensuring security during international convoys.\nD. To build a new temple for the Sikh community, acting as a religious and cultural hub for Sikh residents.", "answer": "A"}
            }
        },
        "B": {
            1: {
                1: {"question": "B1 How did many rickshaw pullers cope with physical suffering?\n\nA. By taking regular breaks\nB. By sleeping more\nC. By turning to opium\nD. By seeking medical help", "answer": "C"},
                2: {"question": "B2 What was the nickname given to the earliest buses in Singapore?\n\nA. Mosquito buses\nB. Small buses\nC. Unlicensed buses\nD. Singapore Bus Services (SBS)", "answer": "A"},
                3: {"question": "B3 What was the primary reason for Chinese coolies wearing dark shades of blue clothing?\n\nA. To show their social status\nB. To blend in with their surroundings\nC. To hide opium stains easily\nD. To follow a cultural tradition", "answer": "C"},
                4: {"question": "B4 What material were the sandals worn by Samsui women usually made of?\n\nA. Cheap Leather\nB. Rubber from disused tyres\nC. Ply Wood\nD. Recycle Plastic Bottle", "answer": "B"},
                5: {"question": "B5 What was the primary purpose of building living quarters colloquially known as \"coolie keng\" in densely-populated areas such as Chinatown?\n\nA. To provide mid tier accommodations for labourers\nB. To offer affordable housing options for labourers\nC. To segregate labourers from other communities\nD. To promote social interaction among labourers", "answer": "B"}
            }
        }
    },
    5: {
        "A": {
            1: {
                1: {"question": "A1 What milestone did Singapore's Hawker Culture achieve in 2020?\n\nA. It was declared a national monument\nB. It was awarded the Faroese Cultural Prize\nC. It was included in UNESCO's Representative List of the Intangible Cultural Heritage of Humanity\nD. It was nominated for UNESCO World Heritage Site", "answer": "C"},
                2: {"question": "A2 What does the Singlish Perpetual Calendar aim to showcase?\n\nA. Common phrases from different cultures\nB. The evolution of formal Malay language\nC. Singapore's national holidays\nD. Singaporean identity through Singlish", "answer": "D"},
                3: {"question": "A3 What did Singapore do as part of its vaccine support for the global community?\n\nA. Donated over 100,000 doses of vaccines to other countries\nB. Supplied raw materials for vaccines to other countries\nC. Shared vaccine research with World Health Organisation\nD. Built a global vaccine stockpile to share with other countries", "answer": "A"},
                4: {"question": "A4 What historic achievement did Yip Pin Xiu accomplish at the 2008 Beijing Paralympic Games?\n\nA. Youngest swimmer in the Paralympics\nB. First Singaporean to win a Paralympic gold medal\nC. First athlete to swim the 50-metre backstroke under 30 seconds\nD. First Singaporean to compete in the Paralympics for 3 different swimming categories", "answer": "B"},
                5: {"question": "A5 Why was the hoisting of the Singapore flag at the UN in 1965 significant?\n\nA. It was a requirement for economic aid\nB. It symbolised Singapore's acceptance into ASEAN\nC. It marked the first international speech by Singapore's PM\nD. It signified Singapore's entry into the international community following its independence", "answer": "D"}
            }
        },
        "B": {
            1: {
                1: {"question": "B1 What is the title of the 1980s postcard that introduces Singapore food culture to international audiences?\n\nA. Eat Like a Local Singaporean\nB. Singapore Local Food\nC. Taste of Singapore\nD. Singapore Food Fiesta", "answer": "B"},
                2: {"question": "B2 How do these culinary artefacts support racial harmony and shared identity in Singapore?\n\nA. By limiting international influences in food\nB. By standardising all dishes to international recipes\nC. By showcasing diverse food traditions from different communities as part of a united national identity\nD. By focusing on only 5 ethnic groups' cuisines", "answer": "C"},
                3: {"question": "B3 What historic summit took place in Singapore in 2018?\n\nA. International Tech Congress\nB. ASEAN Peace Accord\nC. UN Climate Forum\nD. North Korea – United States Summit", "answer": "D"},
                4: {"question": "B4 What was the ASEAN Achievement Millennium Medal awarded for?\n\nA. Mr Lee Kuan Yew's leadership and contribution to ASEAN's formation and Singapore's transformation\nB. Educational outreach in ASEAN schools to provide educational support for the past 10 years\nC. Cultural festival planning with ASEAN for the past 10 years\nD. Military cooperation with the ASEAN countries for the past 10 years", "answer": "A"},
                5: {"question": "B5 How does ASEAN contribute to multiculturalism and peace in Southeast Asia?\n\nA. By enforcing common religious policies across different countries\nB. By promoting economic cooperation between south east asia countries\nC. By fostering peaceful cooperation, shared identity, and inclusive growth among diverse nations\nD. By promoting friendly arms raised competition between member nations to enforce peace", "answer": "C"}
            }
        }
    }
}


STAGE_IMAGES = {
    1: "stage 1.jpeg", 
    2: "stage 2.jpeg", 
    3: "stage 3.jpeg", 
    4: "stage 4.jpeg", 
    5: "stage 5.jpeg", 
}



#endregion

#endregion

#region IMPORTS

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import asyncio

import os
import json
import datetime
from collections import defaultdict
import random
import time
import codecs

from telegram.ext import Defaults
from telegram.constants import ParseMode
from telegram.ext import AIORateLimiter
from telegram.request import HTTPXRequest
from telegram.error import RetryAfter
from telegram.error import BadRequest
from telegram.ext import JobQueue
from telegram.error import RetryAfter, NetworkError

chat_locks = defaultdict(asyncio.Lock)
ask_locks = defaultdict(asyncio.Lock)


#endregion

#region RATE LIMITING

request = HTTPXRequest(
    read_timeout=30,
    write_timeout=30,
    connect_timeout=10,
    pool_timeout=20,
    connection_pool_size=50,  # Reduced further
)

defaults = Defaults(parse_mode=ParseMode.HTML)

question_send_semaphore = asyncio.Semaphore(3)

RATE_LIMIT_DELAY = 0.5  # Increased from 0.1
MAX_CONCURRENT_REQUESTS = 5  # Reduced from 15
rate_limit_semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

onboarding_semaphore = asyncio.Semaphore(3) 

def create_message_log_file():
    global MESSAGE_LOG_FILE
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    MESSAGE_LOG_FILE = f"log_{timestamp}.txt"
    
    # Create the file with headers
    with open(MESSAGE_LOG_FILE, "w") as f:
        f.write("timestamp,action_type\n")
    
    print(f"✅ Message log file created: {MESSAGE_LOG_FILE}")
    
def log_message_action(action_type):
    global MESSAGE_LOG_FILE
    if MESSAGE_LOG_FILE:
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]  # Include milliseconds
            with open(MESSAGE_LOG_FILE, "a") as f:
                f.write(f"{timestamp},{action_type}\n")
        except Exception as e:
            print(f"❌ Failed to log message: {e}")
            
async def safe_send(func, *args, max_retries=3, context=None, **kwargs):
    
    func_name = func.__name__ if hasattr(func, '__name__') else str(func)
    if 'edit' in func_name.lower():
        action_type = "edit"
    elif 'send' in func_name.lower():
        action_type = "send"
    else:
        action_type = "other"
    
    # Helper function to get group info from context
    def get_group_info():
        if context and hasattr(context, 'effective_chat') and context.effective_chat:
            chat_id = context.effective_chat.id
            chat_title = getattr(context.effective_chat, 'title', '')
            if chat_title:
                return f"Group '{chat_title}' (ID: {chat_id})"
            else:
                return f"Chat {chat_id}"
        return None
    
    for attempt in range(max_retries):
        try:
            async with rate_limit_semaphore:
                base_delay = RATE_LIMIT_DELAY * (attempt + 1)
                jitter = random.uniform(0, base_delay * 0.5)
                await asyncio.sleep(base_delay + jitter)
                
                result = await func(*args, **kwargs)
                
                if LOG_MESSAGES == True:
                    log_message_action(action_type)
                
                return result

        except BadRequest as e:
            error_message = str(e).lower()
            group_info = get_group_info()
            group_prefix = f"[{group_info}] " if group_info else ""
            
            # Handle the specific case where message content is identical
            if "message is not modified" in error_message and "exactly the same" in error_message:
                print(f"ℹ️ {group_prefix}Message content unchanged, skipping edit operation")
                # Return None or a success indicator since the message is already in the desired state
                return None
            
            # Handle other BadRequest errors with retries
            if attempt == max_retries - 1:
                print(f"❌ {group_prefix}BadRequest after {max_retries} attempts: {e}")
                raise

            wait_time = (2 ** attempt) + random.uniform(1, 3)
            print(f"⚠️ {group_prefix}BadRequest — retrying in {wait_time:.1f}s (attempt {attempt + 1}): {e}")
            await asyncio.sleep(wait_time)

        except RetryAfter as e:
            group_info = get_group_info()
            group_prefix = f"[{group_info}] " if group_info else ""
            
            if attempt == max_retries - 1:
                print(f"❌ {group_prefix}Max retries exceeded due to rate limiting after {e.retry_after}s")
                raise

            wait_time = e.retry_after + random.uniform(2, 5)
            print(f"⚠️ {group_prefix}Rate limited — retrying in {wait_time:.1f}s (attempt {attempt + 1})")
            await asyncio.sleep(wait_time)

        except NetworkError as e:
            group_info = get_group_info()
            group_prefix = f"[{group_info}] " if group_info else ""
            
            if attempt == max_retries - 1:
                print(f"❌ {group_prefix}NetworkError after {max_retries} retries: {e}")
                raise

            wait_time = (2 ** attempt) + random.uniform(1, 3)
            print(f"🌐 {group_prefix}Network error — retrying in {wait_time:.1f}s (attempt {attempt + 1}): {e}")
            await asyncio.sleep(wait_time)

        except Exception as e:
            group_info = get_group_info()
            group_prefix = f"[{group_info}] " if group_info else ""
            
            if attempt == max_retries - 1:
                print(f"❌ {group_prefix}Failed after {max_retries} attempts: {e}")
                raise

            wait_time = (2 ** attempt) + random.uniform(1, 3)
            print(f"⚠️ {group_prefix}Error — retrying in {wait_time:.1f}s (attempt {attempt + 1}): {e}")
            await asyncio.sleep(wait_time)

    raise RuntimeError("safe_send failed unexpectedly")
#endregion

#region ALL DATA

#region GROUP INTERFACE

#region GROUP IDS

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

async def get_group_link(context=None, group_number=None):
    if group_number is None:
        group_number = context.user_data["group_number"]

    group_link = GROUP_LINKS[group_number]

    return group_link

#endregion

#region GROUP ALLOCATION

ORDERED_GROUP_INDEX = 1
GROUP_POPULATION = 0
CUSTOM_SWITCH = False

group_index_lock = asyncio.Lock()

async def set_group_number(context):
    global ORDERED_GROUP_INDEX, GROUP_POPULATION, CUSTOM_SWITCH

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
                    
    elif GROUP_ALLOCATION_MODE == "custom":
        async with group_index_lock:
            if not CUSTOM_SWITCH:
                group_number = ORDERED_GROUP_INDEX
                GROUP_POPULATION += 1
                
                ORDERED_GROUP_INDEX = (ORDERED_GROUP_INDEX % 4) + 1
                
                if GROUP_POPULATION == (MAX_PER_GROUP * 4):
                    CUSTOM_SWITCH = True
                    ORDERED_GROUP_INDEX = 1  
            else:
                group_number = ORDERED_GROUP_INDEX + 4 
                ORDERED_GROUP_INDEX = (ORDERED_GROUP_INDEX % (MAX_GROUPS - 4)) + 1

    context.user_data["group_number"] = group_number

    return group_number

#endregion

#endregion

#region QUESTION INTERFACE

#region QUESTION DATA


USED_STAGE_QUESTIONS = {
    stage_id: ALL_STAGE_QUESTIONS[stage_id]
    for stage_id in sorted(ALL_STAGE_QUESTIONS.keys())[:MAX_STAGES]
}

async def get_stage_data(context=None, stage=None):
    if stage is None:
        stage = context.chat_data.get("current_stage")

    stage_data = USED_STAGE_QUESTIONS.get(stage)
    return stage_data

async def get_substage_data(context=None, stage=None, substage=None):
    if substage is None:
        substage = context.chat_data.get("current_substage")
    
    stage_data = await get_stage_data(context, stage)
    substage_data = stage_data.get(substage)
    return substage_data

async def get_subset_data(context=None, stage=None, substage=None, subset=None):
    if subset is None:
        subset = context.chat_data.get("current_subset")

    substage_data = await get_substage_data(context, stage, substage)
    subset_data = substage_data.get(subset)

    return subset_data

async def get_question_data(question_id, context=None, stage=None, substage=None, subset=None):
    if subset is None:
        subset = context.chat_data.get("current_subset")

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
    #await switch_subset(context, stage, substage)

    return subset

async def get_subset(context=None, stage=None, substage=None):
    #if stage is None:
        #stage = context.chat_data["current_stage"]

    #if substage is None:
        #substage = context.chat_data["current_substage"]

    #async with subset_lock:
        #subset = CURRENT_SUBSTAGE_SET[stage][substage]

    return 1

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

        min_users = min(suitable_stages, key=lambda x: x[1])[1]
        
        smallest_stages = [
            stage_id for stage_id, users in suitable_stages 
            if users == min_users
        ]
        
        return random.choice(smallest_stages)

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

async def is_image_in_stage(context=None, stage=None):
    if SEND_IMAGES == False:
        return False
    
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

async def is_image_in_question(context, question_id):
    question_data = await get_question_data(question_id, context=context)
    image_filename = question_data.get("image", None)
    
    return image_filename != None

async def get_question_image_file(context, question_id):
    await asyncio.sleep(0.1)
    
    question_data = await get_question_data(question_id, context=context)
    image_filename = question_data.get("image", None)
    
    image_folder = os.path.join(os.path.dirname(__file__), IMAGE_FOLDER)
    image_path = os.path.join(image_folder, image_filename)
    image_file = open(image_path, 'rb')
    
    return  image_file

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
    context.chat_data["tries"] = 0

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
    context.chat_data["current_questions"] = []

async def update_substage_values_correct(context, question):
    if SCORE_UPDATING_MODE == "static":
        context.chat_data["score"] += CORRECT_SCORE
        
    elif SCORE_UPDATING_MODE == "dynamic":
        tries = context.chat_data["tries"]
        score = CORRECT_SCORE + (tries * WRONG_SCORE)
        context.chat_data["score"] += score
        
    context.chat_data["tries"] = 0
        
    context.chat_data["answered_questions"].append(question)
    context.chat_data["current_questions"].remove(question)

async def update_substage_values_wrong(context):
    if SCORE_UPDATING_MODE == "static":
        context.chat_data["score"] += WRONG_SCORE
        
    elif SCORE_UPDATING_MODE == "dynamic":
        context.chat_data["tries"] += 1

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

            if context.user_data.get("group_number") is None:
                await set_group_number(context)
                await send_onboard_instructions(update, context)
                
            else:
                await send_onboard_instructions(update, context)

        else:
            await send_you_already_started(update, context)

#region ONBOARDING BEHAVIOUR

async def send_you_already_started(update, context):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    text = "You are already in a group! \n\n Send /quiz to start the quiz!"

    await safe_send(context.bot.send_message, chat_id, text, reply_to_message_id=message_id, context=context)

async def is_chat_private(update):
    chat_type = update.effective_chat.type

    return chat_type == "private"


async def send_onboard_instructions(update, context):
    chat_id = update.effective_chat.id
    group_number = context.user_data["group_number"]
    group_link = await get_group_link(context)

    text = f"You are in group {group_number}! \n\n1. Join the group using the link: \n{group_link} \n\n2. Wait for everyone else to join"

    await safe_send(context.bot.send_message, chat_id, text)

async def send_help(update, context):
    return False

#endregion

#endregion

#region QUIZ

#region START QUIZ

async def start_quiz_command(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if not await is_chat_private(update):
        chat_id = str(update.effective_chat.id)
        group = await get_group_number(chat_id=chat_id)                        
        
        if GROUP_STATUS[group].get("started") != True:
            async with chat_locks[chat_id]:
                await ask_has_everyone_joined(update, context)
            
        else:
            async with chat_locks[chat_id]:
                await initialise_saved_quiz_values(context, update)
                await print_resuming_stage(context)
                await send_resuming_stage(context)
                
            await ask_next_questions(context)

    else:
        await send_onboard_instructions(update, context)

#region START QUIZ BEHAVIOUR

async def handle_ready(update, query, button_data, context):
    chat_id = update.effective_chat.id
    async with chat_locks[chat_id]:
        new_text = "Quiz starting..."
        await safe_send(query.edit_message_text, text=new_text, context=context)

        await initialise_quiz_values(context, update)
        await print_starting_quiz(context)
        
    await start_next_stage(context)

async def ask_has_everyone_joined(update, context):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    yes_button = InlineKeyboardButton("yes", callback_data="ready")
    keyboard = InlineKeyboardMarkup([[yes_button]])
    text = "Has everyone joined the group?"

    await safe_send(context.bot.send_message, chat_id, text, reply_markup=keyboard, reply_to_message_id=message_id, context=context)


async def initialise_saved_quiz_values(context, update):
    chat_id = str(update.effective_chat.id)
    group_number = await get_group_number(chat_id=chat_id)
    
    context.chat_data["chat_id"] = chat_id
    context.chat_data["group_number"] = group_number
    context.chat_data["current_questions"] = []
    context.chat_data["tries"] = 0
    
    for datum in group_status_data:
        context.chat_data[datum] = GROUP_STATUS[group_number][datum]   


async def send_resuming_stage(context):
    chat_id = context.chat_data["chat_id"]
    stage = context.chat_data["current_stage"]

    text = f"Resuming Chapter {stage}..."

    if await is_image_in_stage(context):
        image_file = await get_stage_image_file(context)
        await safe_send(context.bot.send_photo, chat_id, photo=image_file, caption=text, context=context)

    else:
        await safe_send(context.bot.send_message, chat_id, text, context=context)    
    

async def print_resuming_stage(context):
    group = context.chat_data["group_number"]
    stage = context.chat_data["current_stage"]
    substage = context.chat_data["current_substage"]
    subset = context.chat_data["current_subset"]
    
    print(f"Group {group} resumed part {substage} of stage {stage} (Subset {subset})")

async def print_starting_quiz(context):
    group = context.chat_data["group_number"]
    print(f"Group {group} started quiz")

async def send_starting_quiz(context):
    chat_id = context.chat_data["chat_id"]

    text = "Starting quiz..."
    await safe_send(context.bot.send_message, chat_id, text, context=context)

#endregion

#endregion

#region STAGE SYSTEM

async def end_stage(context):
    await asyncio.sleep(0.5)
    chat_id = context.chat_data["chat_id"]
    
    await update_quiz_values(context)
        
    await print_stage_complete(context)
    await send_stage_complete(context)
    await update_remove_stage_users(context)
    await update_stage_status_remove(context)
    await update_group_status(context)
    await asyncio.sleep(10.0)

    if await is_quiz_complete(context):
        await send_quiz_complete(context)
        await print_quiz_complete(context)

    else:
        await start_next_stage(context)


#region END STAGE BEHAVIOUR

async def send_quiz_complete(context):
    chat_id = context.chat_data["chat_id"]
    score = context.chat_data["score"]

    text=f"Congratulations!🎉 \n\nYou have successfully completed all 5 chapters! 🥳 \n\nFeel free to visit more exhibits at Level 1. \n\nPlease report to Level 2 holding area for PERSCOM photo taking at 1130hr. Thank you!"
    await safe_send(context.bot.send_message, chat_id, text, context=context)

async def print_quiz_complete(context):
    group_number = context.chat_data["group_number"]

    print(f"Group {group_number} finished quiz")

async def send_stage_complete(context):
    stage = context.chat_data["current_stage"]
    score = context.chat_data["score"]
    chat_id = context.chat_data["chat_id"]

    text = f"✅ Chapter {stage} completed! ✅\n\nCurrent score: {score} \n\nPlease take a wefie of the group with the most memorable artifact found in the current chapter. \n\nSend it in this NE Quiz group chat! Thank you!"
    await safe_send(context.bot.send_message, chat_id, text, context=context)

async def print_stage_complete(context):
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    print(f"Group {group} completed stage {stage}")

#endregion

async def start_next_stage(context):
    await asyncio.sleep(0.5)
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
        global NEED_UPDATING 
        NEED_UPDATING = True
        await send_starting_stage(context)
    
    await start_next_substage(context)

#region START STAGE BEHAVIOUR

async def send_starting_stage(context):
    chat_id = context.chat_data["chat_id"]
    stage = context.chat_data["current_stage"]

    text = f"Please proceed to the venue: Chapter {stage}!"

    if await is_image_in_stage(context):
        image_file = await get_stage_image_file(context)
        await safe_send(context.bot.send_photo, chat_id, photo=image_file, caption=text, context=context)

    else:
        await safe_send(context.bot.send_message, chat_id, text, context=context)

async def print_starting_stage(context):
    group_number = context.chat_data["group_number"]
    stage = context.chat_data["current_stage"]

    print(f"Group {group_number} started stage {stage}")

#endregion

#endregion

#region SUBSTAGE SYSTEM

async def end_substage(context):
    await asyncio.sleep(0.5)
    chat_id = context.chat_data["chat_id"]
    async with chat_locks[chat_id]:
    
        await update_stage_values(context)
        await print_substage_complete(context)
        await update_remove_substage_users(context)
        await update_group_status(context)
        global NEED_UPDATING
        NEED_UPDATING = True

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

    await ask_next_questions(context)

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

async def ask_next_questions(context):
    await update_group_status(context)
    subset_data = await get_subset_data(context)
    total_questions = len(subset_data.keys())
    total_current = len(context.chat_data["current_questions"])
    total_answered = len(context.chat_data["answered_questions"])
    total_remaining = total_questions - total_current - total_answered
    
    if total_remaining == 0 and total_current > 0:
        return
    
    elif total_remaining == 0 and total_current == 0:
        await end_substage(context)
        
    elif QUESTION_SEQUENCING_MODE == "1b1":
        chat_id = context.chat_data["chat_id"]
        async with chat_locks[chat_id]:
            next_question = await get_next_question_id(context)
            await ask_question(context, next_question)
            context.chat_data["current_questions"].append(next_question)
        
    elif QUESTION_SEQUENCING_MODE == "2b2":
        chat_id = context.chat_data["chat_id"]
        async with chat_locks[chat_id]:
            
            if total_remaining == total_questions or (total_current == 0 and total_remaining > 1):
                next_question = await get_next_question_id(context)
                await ask_question(context, next_question)
                context.chat_data["current_questions"].append(next_question)
                
                await asyncio.sleep(0.5)
            
                next_next_question = await get_next_question_id(context)
                await ask_question(context, next_next_question)
                context.chat_data["current_questions"].append(next_next_question)
                
            else:
                next_question = await get_next_question_id(context)
                await ask_question(context, next_question)
                context.chat_data["current_questions"].append(next_question)
        
            
async def get_next_question_id(context):
    subset_data = await get_subset_data(context)
    subset_questions = subset_data.keys()
    used_questions = context.chat_data["current_questions"] + context.chat_data["answered_questions"]
    
    for question in subset_questions:
        if question not in used_questions:
            return question


async def ask_question(context, question_id):
    await asyncio.sleep(0.8)
    question_data = await get_question_data(question_id, context)
    question = question_data["question"]
    options = OPTIONS
    chat_id = context.chat_data["chat_id"]

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text= option, callback_data= f"quiz:{question_id}:{option}")]
        for option in options
    ]) 
    text = question
    
    if await is_image_in_question(context, question_id):
        image_file = await get_question_image_file(context, question_id)
        await safe_send(context.bot.send_photo, chat_id, photo=image_file, caption=text, reply_markup=keyboard, context=context)

    else:
        await safe_send(context.bot.send_message, chat_id, text, reply_markup=keyboard, context=context) 

async def handle_question(update, query, response_data, context):
    CORRECT = False
        
    chat_id = str(update.effective_chat.id)
    async with chat_locks[chat_id]:
        async with question_send_semaphore:
            await asyncio.sleep(0.3)
            
            prefix, question_id, selected = response_data.split(":")
            question_id = int(question_id)
            question_data = await get_question_data(question_id, context)
            question = question_data["question"]
            options = OPTIONS
            answer = question_data["answer"]

            if selected == answer and question_id in context.chat_data["current_questions"]:
                CORRECT = True
                await update_substage_values_correct(context, question_id)
                await update_group_status(context)
                await send_answer_correct(query, context, question_id, selected)
                    
            elif selected != answer and question_id in context.chat_data["current_questions"]: 
                await update_substage_values_wrong(context)
                await send_answer_wrong(query, context, question_id, selected)
    
    if CORRECT == True:
        async with ask_locks[chat_id]:
            await ask_next_questions(context)
        

#region HANDLE QUESTION BEHAVIOUR

async def send_answer_correct(query, context, question_id, selected):
    question_data = await get_question_data(question_id, context)
    question = question_data["question"]
    score = context.chat_data["score"]

    new_text = f"{question} \n\nYou selected: {selected} ✅\nScore: {score}"

    if query.message.photo:  # Photo means caption is used
        await safe_send(query.edit_message_caption, caption=new_text, context=context)
    else:
        await safe_send(query.edit_message_text, text=new_text, context=context)


async def send_answer_wrong(query, context, question_id, selected):
    question_data = await get_question_data(question_id, context)
    question = question_data["question"]
    score = context.chat_data["score"]

    old_keyboard = query.message.reply_markup.inline_keyboard
    new_keyboard = InlineKeyboardMarkup([
        [button] for row in old_keyboard for button in row if button.text != selected
    ])
    new_text = f"{question} \n\nYou selected {selected} ❌ \nTry again!"

    if query.message.photo:
        await safe_send(query.edit_message_caption, caption=new_text, reply_markup=new_keyboard, context=context)
    else:
        await safe_send(query.edit_message_text, text=new_text, reply_markup=new_keyboard, context=context)


#endregion

#endregion

#endregion

#region ADMIN MODULE

#region GROUP CHAT DATA

NEED_UPDATING = False

STAGE_STATUS = {
    stage_number: set()
    for stage_number in range(1, MAX_STAGES+1)
}

stage_status_lock = asyncio.Lock()

GROUP_STATUS = {
    group_number: {"current_stage": None, 
                   "completed_stages": [], 
                   "score": 0, 
                   "current_substage" : None,
                   "completed_substages": [],
                   "current_subset": None,
                   "current_substage": None 
                   }
    for group_number in range(1, MAX_GROUPS+1)
}

group_status_lock = asyncio.Lock()


async def update_stage_status_add(context):
    global NEED_UPDATING
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    async with stage_status_lock:
        STAGE_STATUS[stage].add(group)
        NEED_UPDATING = True


async def update_stage_status_remove(context):
    global NEED_UPDATING
    stage = context.chat_data["current_stage"]
    group = context.chat_data["group_number"]

    async with stage_status_lock:
        STAGE_STATUS[stage].discard(group)
        NEED_UPDATING = True

group_status_data = ["current_stage",
                     "completed_stages",
                     "score",
                     "current_substage",
                     "completed_substages",
                     "current_subset",
                     "answered_questions",
                     "started"]

async def update_group_status(context):    
    group = context.chat_data["group_number"]

    async with group_status_lock:
        if not await is_quiz_complete(context):
            for data in group_status_data:
                GROUP_STATUS[group][data] = context.chat_data[data]

        else:
            score = context.chat_data["score"]
            GROUP_STATUS[group] = f"Completed quiz. Score: {score}"
            
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
        NEED_UPDATING = False
        await update_dashboard(context.application)

#endregion

#region BROADCAST

async def broadcast_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != ADMIN_CHAT_ID:
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast Group 1:\\nGroup 2:")
        return

    raw_text = " ".join(context.args)

    # Replace escaped "\n" strings with actual newlines
    message = raw_text.replace("\\n", "\n")

    if len(message) > 4096:
        await update.message.reply_text("❌ Message too long (exceeds 4096 characters)")
        return

    print(f"📣 Broadcasting:\n{message}")

    success = 0
    failed = 0

    for chat_id in ALL_CHAT_IDS:
        try:
            await safe_send(context.bot.send_message, chat_id=chat_id, text=message, parse_mode=None)
            success += 1
        except Exception as e:
            print(f"❌ Failed to send to {chat_id}: {e}")
            failed += 1

    if success == MAX_GROUPS:
        await update.message.reply_text("✅ Sent to every chat")
    else:
        await update.message.reply_text(f"✅ Sent to {success} chats. ❌ Failed: {failed}")


            



#endregion

#endregion

#region SAVE FILE

file_write_lock = asyncio.Lock()

async def save_state():
    async with file_write_lock:
        try:
            with open(SAVE_FILE, "w") as f:
                json.dump(GROUP_STATUS, f)
        except Exception as e:
            print(f"❌ Failed to save quiz state: {e}")
        
def load_state():
    global GROUP_STATUS, NEED_UPDATING
    
    try:
        with open(SAVE_FILE, "r") as f:
            loaded_data = json.load(f)
            
        for group_key, group_data in loaded_data.items():
            group_number = int(group_key)
            if 1 <= group_number <= MAX_GROUPS:
                GROUP_STATUS[group_number] = group_data
                
        NEED_UPDATING = True
            
        print(f"✅ Quiz state loaded")
            
    except Exception as e:
        print(f"❌ Failed to load quiz state: {e}")

def reset_state():
    global GROUP_STATUS, NEED_UPDATING
    
    try:
        GROUP_STATUS = {
            group_number: {
                "current_stage": None, 
                "completed_stages": [], 
                "score": 0, 
                "current_substage": None,
                "completed_substages": [],
                "current_subset": None,
                "answered_questions": []
            }
            for group_number in range(1, MAX_GROUPS+1)
        }
        
        NEED_UPDATING = True
        
        print("✅ Quiz state reset to default values")
        
    except Exception as e:
        print(f"❌ Failed to reset quiz state: {e}")

#region BUTTON HANDLER

handlers = {
        "ready": handle_ready,
        "quiz": handle_question
    }

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    try:
        await query.answer()
    except BadRequest as e:
        if "too old" in str(e).lower():
            return
        raise
    except Exception as e:
        print(f"❌ Error answering query: {e}")
        return

    button_data = query.data
    prefix = button_data.split(":")[0] if ":" in button_data else button_data
    handler = handlers.get(prefix)

    await handler(update, query, button_data, context)



#endregion

#region RUN BOT

if __name__ == "__main__":
    if MESSAGE_LOG_FILE == None and LOG_MESSAGES == True:
        create_message_log_file()
        
    job_queue = JobQueue()
    
    rate_limiter = AIORateLimiter(
        max_retries=3  # Only this parameter is valid
    )

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .defaults(defaults)
        .rate_limiter(rate_limiter)
        .concurrent_updates(50)
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
    interval=20,      
    first=5,
    job_kwargs={"max_instances": 1}           
)

    if LOAD_SAVE_FILE == True:
        load_state()
    elif RESET_SAVE_FILE == True:
        reset_state()

    print("✅ Polling 10...")

    app.run_polling()

#endregion