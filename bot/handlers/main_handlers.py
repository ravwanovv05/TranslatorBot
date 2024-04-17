from aiogram import types
from api.telegram_users import TelegramUser
from bot.reply_buttons.after_start_buttons import buttons


async def start_handler(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else None
    username = message.from_user.username if message.from_user.username else None
    language = message.from_user.language_code
    telegram_id = message.from_user.id
    name = first_name + " " + last_name if last_name else first_name

    telegram_user = TelegramUser(first_name, language, telegram_id, last_name, username)
    telegram_user.create_user()

    await message.answer(f"Xush kelibsiz, {name}.", reply_markup=buttons())


async def help_handler(message: types.Message):
    text = "Tilni sozlash orqali tilni tanlang va istalgan tilda matin kiriting bot uni tanlagan tilingizga tarjima qilib beradi"
    await message.answer(text)