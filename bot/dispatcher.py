import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

loop = asyncio.get_event_loop()

bot = Bot(token=os.getenv('BOT_TOKEN'), loop=loop)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
