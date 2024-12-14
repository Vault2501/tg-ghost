import sys
import asyncio
import random
import time
from telethon import TelegramClient, events
#sys.path.append('../GPTIntegration')
from gptintegration import GPTIntegration

# Your user ID
api_id = 0987654321 
# Telegram PAI hash. Replace with your own
api_hash = '1234567890' 
system_message = "Your are an assistant. Speak German."

# Minimal time to wait before answering
wait_min = 60 
# Maximum time to wait before answering
wait_max = 360 
# Users the bot will reply to, replace with valid users ids
config_users = [00000000]
# Bots the bot will reply to, replace with valid bot ids
config_bots = [00000000]
# Chats the bot will reply in. Replace with group ids
config_chats = [00000000]

# gpt integration - replace 0000000000 with your ChatGPT API code
gpt_integration = GPTIntegration('000000000000')


client = TelegramClient('session_name', api_id, api_hash)
client.start()


@client.on(events.NewMessage(from_users=config_users, chats=config_chats))
@client.on(events.NewMessage(from_users=config_bots))
@client.on(events.MessageEdited(from_users=config_bots))

async def handler(event):
    user_message = event.raw_text
    msg = event.message
    sender = await event.get_sender()
    print("\n\nUser: ", sender.username, "ID: ", sender.id)
    print("Message Text: ", user_message)
    print("Message: ", msg, "\n")

    dice = random.randint(1,6)
    print("dice says: ", dice)

    if (user_message != '...') and ((dice >= 5) or (msg.mentioned)):
        delay = random.randint(wait_min,wait_max)
        print("Triggered! - waiting for ", 2*delay, "seconds before answering\n")
        await asyncio.sleep(delay)

        async with client.action(event.chat_id, 'typing'):
            await asyncio.sleep(delay)
            print("Querying LocalAI")
            response = gpt_integration.query_gpt(system_message, user_message)
            reply = response.choices[0].message.content.strip('\"')
            print("Reply is: ", reply)

        result = await client.send_message(entity=event.chat_id, reply_to=msg.id, message=reply)
        print("Result: ", result)

client.run_until_disconnected()
