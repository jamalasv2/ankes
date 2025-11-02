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
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmission=7,
        )
    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        LOGGER(__name__).info(f"ankes [ {self.name} ] diaktifkan")

    async def stop(self):
        await super().stop()

app = Bot()

