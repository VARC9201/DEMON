import config
from DEADLYSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, deadlyversion, SUDOERS
from telethon import events, version, Button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://graph.org/file/58fe560a47428a2a591fc.mp4"

hl = config.CMD_HNDLR

DEADLY = " ᴅᴇᴍᴏɴ ꜱᴘᴀᴍ ʜᴇʀᴇ 🥀\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **ᴅᴇᴍᴏɴʙᴏᴛ ᴠᴇʀsɪᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"

async def send_alive_message(client, event):
    Blaze = [
        [Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/+XxS3X3ayLqQ5Njdk"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/+dKGCo7oumwYwZDNl")],
    ]
    await client.send_file(event.chat_id, DEADLY_PIC, caption=DEADLY, buttons=Blaze)

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive0(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT0, event)
    else:
        await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴍᴏɴ-ꜱᴘᴀᴍ ʙᴏᴛꜱ**")

# Handlers for BOT1 to BOT9

# BOT1
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive1(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT1, event)
    else:
        await event.reply("**ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴍᴏɴ-ꜱᴘᴀᴍ ʙᴏᴛꜱ**")

# BOT2
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive2(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT2, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# Similarly, continue for BOT3 to BOT9
# BOT3
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive3(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT3, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT4
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive4(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT4, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT5
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive5(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT5, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT6
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive6(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT6, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT7
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive7(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT7, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT8
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive8(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT8, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")

# BOT9
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive9(event):
    if event.sender_id in SUDOERS:
        await send_alive_message(BOT9, event)
    else:
        await event.reply("**ᴅᴇᴘʟʏ ʏᴏᴜʀ ᴏᴡɴ ᴅᴇᴀᴅʟʏ-ꜱᴘᴀᴍʙᴏᴛ!**")
