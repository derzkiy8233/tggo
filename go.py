from config import *
from time import sleep
from pyrogram import Client, filters, sync
from pyrogram.errors import FloodWait
import sys
client = Client('ghoul-session', api_id, api_hash)

client.start()

client.stop()

print('Готово! Напиши в тг "Spam" ')


@client.on_message(filters.regex('spam|Spam|SPAM') & filters.me)
def ghoul_spam_handler(client, message):
    i = 1000 
    while i > 0:
        try:
            client.send_message(message.chat.id, f'Осталось {i-1} сообщений до конца (Это спам детка)')
        except FloodWait as e:
            sleep(e.x)

        i -= 1
        sleep(0)        

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)

@client.on_message(filters.command(ghoul_table_command, prefixes=command_prefixes) & filters.me)
def ghoul_table_handler(client, message):
    i = 1000
    while i > 62:
        try:
            text = f'{i} - 7 = {i-7}'
            for j in range(1,10):
                text += f'\n{i-7*j} - 7 = {i-7*(j+1)}'
            message.edit_text(f'`{text}`')
            sleep(sleep_time_ghoul)
        except FloodWait as e:
            sleep(e.x)

        i -= 7

    if(end_message != ''):
        client.send_message(message.chat.id, end_message)


client.run() 
