import asyncio
import importlib

from pyrogram import idle

from config import LOGGER
from Ankes import app
from Ankes.modules import ALL_MODULES


async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Ankes.modules" + all_module)
        LOGGER("JamalasxPlugins").info("berhasil memuat semua modul")
    await idle()
    await app.stop()
    LOGGER("JamalasxAnkes").info("bot ankes dinonaktifkan")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

