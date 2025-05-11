import yt_dlp
import os
import glob
import asyncio
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from Amo import keep_alive

keep_alive()

# مشخصات ربات تلگرام
api_id = 25444013
api_hash = "bfbb5734526653271b8a106d046b5754"
bot_token = "6032647077:AAHDvOSf1o4zc5zqsKV5eh6jTue8Lpc_Xpk"

app = Client(
    "amo_inst",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

async def download_instagram_reel(url):
    d_name = None
    output_template = '%(title)s.%(ext)s'

    ydl_opts = {
        'outtmpl': output_template,
        'quiet': True,
        'noplaylist': True,
        'merge_output_format': 'mp4',
        #'cookies': 'cookies.txt',  # فایل کوکی رو کنار سورس بذار
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36'
        }
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'output')
            possible_files = glob.glob(f"{title}*.mp4")
            if possible_files:
                d_name = possible_files[0]
        except Exception as e:
            print("خطا در دانلود:", e)

    return d_name

@app.on_message(filters.text)
async def send_file(bot, message):
    chat_id = message.chat.id
    mes = message.text
    if 'instagram.com' in mes:
        await app.send_message(chat_id, "در حال دانلود ویدیو . . .")
        name = await download_instagram_reel(mes)
        if name and os.path.exists(name):
            await app.send_video(chat_id, name)
            os.remove(name)
            await app.send_message(chat_id, "انجام شد")
        else:
            await app.send_message(chat_id, "خطا در دانلود فایل. شاید کوکی اشتباهه یا ویدیو پرایویته.")

app.run()