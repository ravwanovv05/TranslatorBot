from aiogram import types
from api.telegram_users import TelegramUser
from bot.dispatcher import bot, dp
from bot.reply_buttons.after_start_buttons import buttons


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

    telegram_user = TelegramUser(first_name, language, telegram_id, last_name, username)
    telegram_user.create_user()

    await message.answer(f"Xush kelibsiz, {name}.", reply_markup=buttons())


async def help_handler(message: types.Message):
    text = "Tilni sozlash orqali tilni tanlang va istalgan tilda matin kiriting bot uni tanlagan tilingizga tarjima qilib beradi"
    await message.answer(text)