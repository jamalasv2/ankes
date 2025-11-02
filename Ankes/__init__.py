from pyrogram import Client, filters

from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    LOGGER,
)

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="ankes",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
        )




