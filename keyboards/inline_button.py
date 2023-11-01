from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def save_music():
    markup = InlineKeyboardMarkup()
    music_save = InlineKeyboardButton(
        'Сохранить', callback_data='save_music'
    )
    markup.add(music_save)
    return markup


async def save_meme():
    markup = InlineKeyboardMarkup()
    meme_save = InlineKeyboardButton(
        'Сохранить', callback_data='save_meme'
    )
    markup.add(meme_save)
    return markup


async def profile_button():
    markup = InlineKeyboardMarkup()
    saved_music_button = InlineKeyboardButton('Сохранёные музыки', callback_data='saved_musics_call')
    saved_meme_button = InlineKeyboardButton('Сохранёные мемы', callback_data='saved_meme_call')
    markup.add(saved_music_button, saved_meme_button)
    return markup


async def delete_saved_music():
    markup = InlineKeyboardMarkup()
    delete_music_button = InlineKeyboardButton('Удалить', callback_data='delete_music_call')
    markup.add(delete_music_button)
    return markup
