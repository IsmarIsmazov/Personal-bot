from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton


async def start_button():
    markup = ReplyKeyboardMarkup()
    menu_button = InlineKeyboardButton(text="Меню")
    profile_button = InlineKeyboardButton(text="Профиль")
    music_button = InlineKeyboardButton(text='Музыка')
    meme_button = InlineKeyboardButton(text='Мем')

    markup.add(profile_button)
    markup.add(meme_button, music_button)
    markup.add(menu_button)
    return markup



