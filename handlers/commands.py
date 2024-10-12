from pyrogram import Client, filters
import os
import sys
from configs import Config

OWNER_ID = Config.OWNER_ID
BOT_TOKEN = Config.BOT_TOKEN

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def helpMessage():
    return """Kirimkan Bot Link Video Yang Akan Di Download

/start - Memulai bot
/help - Menampilkan perintah bot
/reboot - Restart bot *(recommended) stop proses record yang berjalan terlebih dahulu
/proses - Menampilkan proses yang sedang berjalan
/status - Menampilkan status bot
/stop{pdid} - Menghentikan proses yang sedang berjalan
"""

async def helpCommand(client, message):
    if message.from_user.id in OWNER_ID:
        await message.reply_text(helpMessage())

async def rebootCmd(client, message):
    if message.from_user.id in OWNER_ID:
        await message.reply_text("Done!")
        restartBot()

async def startCommand(client, message):
    if message.from_user.id in OWNER_ID:
        await message.reply_text("Bot Aktif, Kirimkan Link Video Yang Akan Di Download\n\n/help - Untuk Melihat Perintah Bot")
    else:
        await message.reply_text("""Kamu tidak memiliki akses untuk bot ini""")
