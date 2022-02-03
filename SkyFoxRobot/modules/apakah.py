import random
from SkyFoxRobot.events import register
from SkyFoxRobot import telethn

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu pler"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))



YANSEN_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu pler"
                 ]


@register(pattern="^arka ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('apa sayang')
        return
    await event.reply(random.choice(YANSEN_STRING))




@register(pattern="^arka ganteng ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('owner ganteng @laz1yy')
        return
    await event.reply(random.choice(YANSEN_STRING))

