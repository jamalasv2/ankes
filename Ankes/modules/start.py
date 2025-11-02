from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import Message

from Ankes import app


@app.on_message(filters.command(["start"]) & filters.private)
async def start_pm(client, message: Message, _):
    await message.reply("hai kampang")
