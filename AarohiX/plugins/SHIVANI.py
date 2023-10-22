from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from AarohiX import app
import string
from strings import get_command

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

SHIVANI = [" **╔════════════════❍⊱
║┏━━━━━━➣
║ ┣⪼ 😱𝚁𝚎𝚊𝚕 𝙽𝚊𝚖𝚎- 𝐒ԋɿ‌ꪜ‌ᴀ‌ղ𝒊
║ ┣⪼ ❤ᴛᴇʟᴇɢʀᴀᴍ ɴᴀᴍᴇ- 𝐒ԋɿ‌ꪜ‌ᴀ‌ղ𝒊
║┗━━━━━━➣ 
       ❤️‍🔥  M SC ❤️‍🔥
   ┏━━━━━━➣
║  ┣⪼  ⚡ 19 Dec  𝐇𝐁𝐃⚠️
║  ┣⪼ 🛡Ɩąŋɠųąɠɛ : ɧıŋɖı 🔠 ɛŋɠƖıʂɧ
║┗━━━━━━➣
       🌐Fɾσɱ - KARNATAKA
       ⚡ʙғ - 🤣
         🌟 ᏴᎡϴͲᎻᎬᎡ ❤️‍🔥❤️‍🔥 @DEV1L_999
║╔═════ஜ۩۞۩ஜ════╗
║     B‌o‌t‌s‌ 
║              @ShivaniChatBot
║              @ShivanixMusicBot     
║╚═════ஜ۩۞۩ஜ════╝
╚════════════════❍⊱** "]

# Command of SHIVANI
SHIVANI_COMMAND = get_command("SHIVANI_COMMAND")

@app.on_message(
    filters.command(SHIVANI_COMMAND)
    & filters.group
    & ~filters.edited & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHIVANI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥰𝐒ԋɿ̆ꪜ͜ᴀ͎ղ𝒊🥰", url=f"https://t.me/SHIVANI_SHIVANI_123"),
                    InlineKeyboardButton(
                        "💝𝐆𝐫𝐨𝐮𝐩💝", url=f"https://t.me/ShivaniXMusicS")
                    
                ]
            ]
        ),
    )

@app.on_message(
    filters.command(SHIVANI_COMMAND)
    & filters.private
    & ~filters.edited & filters.private & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        text = random.choice(SHIVANI),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥰𝐒ԋɿ̆ꪜ͜ᴀ͎ղ𝒊]🥰", url=f"https://t.me/SHIVANI_SHIVANI_123"),
                    InlineKeyboardButton(
                        "💝𝐆𝐫𝐨𝐮𝐩💝", url=f"https://t.me/ShivaniXMusicS")
                    
                ]
            ]
        ),
    )
