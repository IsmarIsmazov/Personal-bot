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


async def games_choice():
    markup = InlineKeyboardMarkup()
    dice_game = InlineKeyboardButton('🎲', callback_data='dice_game_call')
    bowling_game = InlineKeyboardButton('🎳', callback_data='bowling_game_call')
    football_game = InlineKeyboardButton('⚽', callback_data='football_game_call')
    basketball_game = InlineKeyboardButton('🏀', callback_data='basketball_game_call')
    darts_game = InlineKeyboardButton('🎯', callback_data='darts_game_call')
    jackpot_game = InlineKeyboardButton('🎰', callback_data='jackpot_game_call')
    markup.add(dice_game, bowling_game, football_game)
    markup.add(basketball_game, darts_game, jackpot_game)
    return markup
