# Telegram-python-quiz-bot

Made for my Army Branch for a trip to a National Mueseum. Through the telegram API, The chatbot will direct groups to least occupied exhibits to prevent crowding, then send them MCQ questions and images. 

Supports 70+ concurrent users.  
Involves asynchronous concurrency control using asyncio, semaphores, and retry logic, to ensure system stability under high traffic and telegram rate limiting.  
Features a real-time admin monitoring dashboard to track quiz progression, team performance, and completion status. It can also broadcast messages to each group.  
Designed a stage-based quiz engine with persistent state management by saving progress to an external JSON, allowing for resumption if interrupted.  

Requires setting up of a telegram bot and its token, as well as the chat IDs of the group chats that the bot is added to, and invite links that it can send out.  
After running the program, send /start to the bot to begin, it should send an invite link to a groupchat.  
In the groupchat, send /quiz to start the quiz.  
