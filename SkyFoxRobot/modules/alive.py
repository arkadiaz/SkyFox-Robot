import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SkyFoxRobot.events import register
from SkyFoxRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/281fbf2e19c36b34d4f40.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm SkyFox Robot.** \n\n"
    TEXT += "ð  **I'm Working Properly** \n\n"
    TEXT += f"ð  **My Master : [Arka](https://t.me/laz1yy)** \n\n"
    TEXT += f"ð  **Library Version :** `{telever}` \n\n"
    TEXT += f"ð  **Telethon Version :** `{tlhver}` \n\n"
    TEXT += f"ð  **Pyrogram Version :** `{pyrover}` \n\n"
    TEXT += "**Thanks For Adding Me Here â¤ï¸**"
    BUTTON = [
        [
            Button.url("Êá´Êá´â", "https://t.me/SkyFoxyRobot?start=help"),
            Button.url("sá´á´á´á´Êá´â", "https://t.me/arkabotsupport"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
