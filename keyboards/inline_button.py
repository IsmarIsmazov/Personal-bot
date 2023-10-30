from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def save_music():
    markup = InlineKeyboardMarkup()
    music_save = InlineKeyboardButton(
        'Сохранить', callback_data='save_music'
    )
    markup.add(music_save)
    return markup
