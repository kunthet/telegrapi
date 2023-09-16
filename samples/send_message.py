# -*- coding: utf-8 -*-

import os
from dotenv import load_dotenv
import json
from telegrapi import Chat, TEngine


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

        
if __name__ == '__main__':
    
    bot = TEngine(TELEGRAM_TOKEN)
    channel = Chat(CHAT_ID, bot)
    
    # to send file into channel
    filepath_to_send = "./telegrapi/api.py"
    caption='test sending file.'
    result = channel.file(filepath_to_send, caption).send()
    print(result)
    
    # to send text message into channel
    message = json.dumps(result, ensure_ascii=False, indent=4)
    result = channel.message(message).send()
    print(result)