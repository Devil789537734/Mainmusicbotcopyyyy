from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="❣️ʜᴇʟᴩ❣️",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="❤‍🔥sᴇᴛᴛɪɴɢs❤‍🔥", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 💪 💖", url=f"https://t.me/DEV1L_999"),
            InlineKeyboardButton(
                text="🥰 ᴍʏ ʟɪғᴇʟɪɴᴇ🥰", url=f"https://t.me/ShivaniXMusicS"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ[ᴅɪʟ]💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🥰R̸e̸p̸o̸🥰", url=f"https://telegra.ph/file/440427330b7871341f2cf.mp4"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🥺Ꮧꮄꮄ Ꮇꮛ ꮦꭷ Ꭹꭷꮼꮢ Ꮆꮢꭷꮼꭾ 🥺",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🥺ʜᴇʟᴩ🥺", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💖 𝐒ԋɿ̆ꪜ͜ᴀ͎ղ𝒊 💖", url=f"https://t.me/SHIVANI_SHIVANI_123"),
            InlineKeyboardButton(
                text="🥰 💪 🥰", url=f"https://t.me/DEV1L_999"
            ),
        ],
        [
            InlineKeyboardButton(text="💝ᴍᴀɪɴᴛᴀɪɴᴇʀ💝", user_id=OWNER),
            InlineKeyboardButton(
                text="🧐R̸e̸p̸o̸🧐", url=f"https://telegra.ph/file/440427330b7871341f2cf.mp4"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="🥺 Ꮇꮧꮥꭷꭷꮇ Ꮭꮧꮄꮶꭵ 🥺", url=f"https://t.me/SHIVANI_SHIVANI_123"
                )
        ],
     ]
    return buttons
