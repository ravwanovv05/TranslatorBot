from aiogram.types import ReplyKeyboardMarkup


def buttons():
    design = [
        ['Tilni sozlash 🌐', 'Mening tilim 👁‍🗨'],
        ['Yordam 🆘', 'Fikr-mulohaza ✒']
    ]
    mrk = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return mrk
