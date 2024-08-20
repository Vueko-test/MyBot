import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = "7223907999:AAHdw5TPdslXR503nHC9CxX7Bso1ve5AjUk"

bot = Bot(token=TOKEN)

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", parse_mode=ParseMode.HTML)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())