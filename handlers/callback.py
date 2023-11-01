import os

from aiogram import types, Dispatcher
from config import bot
from constants import music_dir
from keyboards import inline_button
from database.sql_commands import Database


async def save_music_call(call: types.CallbackQuery):
    file_name = call.message.audio.file_name
    file_dir = os.path.join(music_dir, file_name)
    Database().sql_insert_music_list_command(telegram_id=call.from_user.id,
                                             music=file_dir)
    await call.message.answer('Вы сохранили музыку!')


async def saved_musics(call: types.CallbackQuery):
    user_id = call.from_user.id
    musics = Database().sql_select_music_list_command(telegram_id=call.from_user.id)
    if musics:
        await bot.send_message(chat_id=user_id, text="Пожалуйста подождите, музыки грузится")
        for music in musics:
            music_file = open(music['music'], 'rb')
            await bot.send_audio(chat_id=user_id, audio=music_file, reply_markup=await inline_button.delete_saved_music())
    else:
        await bot.send_message(chat_id=call.from_user.id, text='Вы еще не сохранили ни одной музыки')


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(save_music_call, lambda call: call.data == "save_music")
    dp.register_callback_query_handler(saved_musics, lambda call: call.data == "saved_musics_call")
