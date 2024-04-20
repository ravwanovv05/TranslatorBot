import os
from aiogram import types
from api.telegram_users import TelegramUser
from bot.dispatcher import bot, dp
from bot.reply_buttons.after_start_buttons import buttons
from telegram_users_DB.function_DB import read_json_data, write_json_data

WEBHOOK_HOST = 'https://c825-178-218-201-17.ngrok-free.app'  # Domain name or IP addres which your bot is located.
WEBHOOK_PORT = 443  # Telegram Bot API allows only for usage next ports: 443, 80, 88 or 8443
WEBHOOK_URL_PATH = '/webhook'  # Part of URL
WEBHOOK_URL = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{WEBHOOK_URL_PATH}"
WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001


async def on_startup(app):
    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()
        await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(app):
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()


async def start_handler(message: types.Message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name if message.from_user.last_name else None
    username = message.from_user.username if message.from_user.username else None
    language = message.from_user.language_code
    telegram_id = message.from_user.id
    name = first_name + " " + last_name if last_name else first_name

    file_path = os.path.abspath('telegram_users_DB/telegram_users.json')

    telegram_users_data = read_json_data(file_path)
    telegram_users_id = []

    for info in telegram_users_data:
        telegram_users_id.append(info['telegram_id'])

    if telegram_id not in telegram_users_id:
        telegram_users_data.append(
            {
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "lang_code": language,
                "telegram_id": telegram_id
            }

        )
        write_json_data(file_path, telegram_users_data)

        telegram_user = TelegramUser(first_name, language, telegram_id, last_name, username)
        telegram_user.create_user()

    await message.answer(f"Xush kelibsiz, {name}.", reply_markup=buttons())


async def help_handler(message: types.Message):
    text = "Tilni sozlash orqali tilni tanlang va istalgan tilda matin kiriting bot uni tanlagan tilingizga tarjima qilib beradi"
    await message.answer(text)