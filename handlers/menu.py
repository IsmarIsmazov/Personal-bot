import random
from aiogram import types, Dispatcher
from config import bot, ADMINS
from constants import music_files, meme_files
from database.sql_commands import Database
from keyboards.inline_button import save_music, save_meme, profile_button
from keyboards.reply_button import menu_button


async def menu(message: types.Message):
    await message.answer("*Вы вошли в меню*", parse_mode='MarkdownV2', reply_markup=await menu_button())
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

async def profile(message: types.Message):
    user = Database().sql_select_telegram_users_command(telegram_id=message.from_user.id)
    if user:
        user_id = user[0]['telegram_id']
        user_username = user[0]['username']
        await message.answer(f'Вы вошли в свой профиль\nВаш ID: {user_id}\nВаш никнейм: @{user_username}',
                             reply_markup=await profile_button())
    else:
        await message.answer('Напишите /start  для начала работы с ботом')
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

async def music(message: types.Message):
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")
    random_music = random.choice(music_files)
    music_list = open(random_music, 'rb')
    await bot.send_message(chat_id=message.from_user.id, text='*Подождите пожалуйста, музыка грузится\.\.\.\n'
                                                              'Это может занять от 5 до 20 секунд*',
                           parse_mode='MarkdownV2')
    await bot.send_audio(chat_id=message.from_user.id, audio=music_list, reply_markup=await save_music())


async def playlist(message: types.Message):
    pass


async def meme(message: types.Message):
    random_meme = random.choice(meme_files)
    meme_list = open(random_meme, 'rb')
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=meme_list, reply_markup=await save_meme())
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")

def register_menu_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, regexp=r'^Меню$')
    dp.register_message_handler(profile, regexp=r'^Профиль$')
    dp.register_message_handler(music, regexp=r'^Музыка$')
    dp.register_message_handler(meme, regexp=f'^Мем$')
