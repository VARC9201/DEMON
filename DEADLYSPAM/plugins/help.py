import config
from DEADLYSPAM import BOT0, SUDOERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
import asyncio
import sys
import heroku3


hl = config.CMD_HNDLR
 
HELP_PIC = "https://graph.org/file/ce053174246e4fe027137.jpg"

DEAD_HELP = "ᴅᴇᴍᴏɴ-ꜱᴘᴀᴍ ʙᴏᴛ 🥀\n\n"
DEAD_HELP += f"ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ ɪɴ ᴅᴇᴍᴏɴ-ꜱᴘᴀᴍ ʙᴏᴛ 🪶\n\n"
DEAD_HELP += f" ↧ sᴘᴀᴍʙᴏᴛ 𝙲𝙼𝙳𝚂 ↧\n\n"
DEAD_HELP += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n `!delsudo` to delete someone from sudolist\n\n"
DEAD_HELP += f" ↧ 𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳 ↧\n\n"
DEAD_HELP += f" `!leave` - to leave public/private channel/groups\n\n" 
DEAD_HELP += f" ↧ 𝚂𝙿𝙰𝙼 𝙲𝙼𝙳𝚂 ↧\n\n"
DEAD_HELP += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"
DEAD_HELP += f" !pornspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ😂 ↧\n\n"
DEAD_HELP += f"© @KANU_XD\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
  if event.sender_id in SUDOERS:
     await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEAD_HELP,
                                  buttons=[
        [
        Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/+AWn8gpMeZndjNzM0"),
        Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/+dKGCo7oumwYwZDNl")
        ],
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
