from pyrogram import filters
from Ankes import app


@app.on_message(filters.command(["word"]))
async def bl_word(client, message: Message):
  


