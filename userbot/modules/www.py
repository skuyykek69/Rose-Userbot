# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import time
import redis

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Tunggu Sebentar.__")
    await pong.edit("__Tunggu Sebentar..__")
    await pong.edit("__Tunggu Sebentar...__")
    await pong.edit("__Tunggu Sebentar....__")
    await pong.edit("__Tunggu Sebentar.__")
    await pong.edit("__Tunggu Sebentar..__")
    await pong.edit("__Tunggu Sebentar...__")
    await pong.edit("__Tunggu Sebentar....__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**{ALIVE_NAME}**        \n"
                    f"**➾Kecepatan : ** '%sms'  \n"
                    f"**➾Branch : ** 'Rose-Userbot` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-ꜱɪɢɴᴀʟ- :** "
                    f"`%sms` \n"
                    f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🌹Rose-Userbot🌹**\n"
                    f"➾ __Signal__    __:__ "
                    f"`%sms` \n"
                    f"➾ __Uptime__ __:__ "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Mohon Menunggu.__")
    await pong.edit("__Mohon Menunggu..__")
    await pong.edit("__Mohon Menunggu...__")
    await pong.edit("__Mohon Menunggu....__")
    await pong.edit("__Mohon Menunggu.__")
    await pong.edit("__Mohon Menunggu..__")
    await pong.edit("__Mohon Menunggu...__")
    await pong.edit("__Mohon Menunggu....__")
    await pong.edit("💫")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🌹 འօʂҽ-Աʂҽɾҍօէ  🌹**\n\n"
                    f"** ▹  Sɪɢɴᴀʟ   :** "
                    f"`%sms` \n"
                    f"** ▹  Uᴘᴛɪᴍᴇ  :** "
                    f"`{uptime}` \n"
                    f"** ▹  Oᴡɴᴇʀ   :** `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**✿**)
    await pong.edit("**✿✿**)
    await pong.edit("**✿✿✿**)
    await pong.edit("**◕‿- PONG!!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f""**🌹 Rose Ping 🌹**\n"
                    f"❊ **Ping:** "
                    f"`%sms` \n"
                    f"❊ **Uptime:** "
                    f"`{uptime}` \n"
                    f"**✦҈͜͡➳ My Name:** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **{ALIVE_NAME} ** \n"
                   f"✧ **Dimulai Pada :**  \n"
                   f"`{result['timestamp']}` \n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✧ **BOT:** 🌹འօʂҽ - Աʂҽɾҍօէ🌹")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@ register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("**☢️PONG PING PONG☢️**")
    await asyncio.sleep(1)
    await pong.edit("💫")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**🌹RoseName : {ALIVE_NAME}**\n`%sms`" % (duration))


CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` | `.lping` | `.xping` | `.pings` | `.sping`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.speed`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.pong`\
         \n↳ : Sama Seperti Perintah Ping."})
