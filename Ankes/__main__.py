import asyncio
import importlib

from pyrogram import idle
from config import LOGGER
from Ankes import app


async def main():
    await app.start()
    await idle()
    await app.stop()
    LOGGER("JamalasxAnkes").info("ankes dinonaktifkan")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

