import asyncio
from importlib import import_module

from pyrogram import idle

from config import LOGGER
from Ankes import app
from Ankes.modules import loadModule

HELP_COMMANDS = {}

async def main():
    await app.start()
    modules = loadModule()
    for mod in modules:
        imported_module = import_module(f"Ankes.modules.{mod}")
        module_name = getattr(imported_module, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported_module
            LOGGER("JamalasxPlugins").info("berhasil memuat semua modul")
    await idle()
    await app.stop()
    LOGGER("JamalasxAnkes").info("bot ankes dinonaktifkan")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

