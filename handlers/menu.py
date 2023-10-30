import random
from aiogram import types, Dispatcher
from config import bot, ADMINS
from constants import music_files
from keyboards.inline_button import save_music
from keyboards.reply_button import profile_button


async def menu(message: types.Message):
    await message.answer("*Вы вошли в меню*", parse_mode='MarkdownV2')


async def profile(message: types.Message):
    await message.answer('*Вы вошли в свой профиль*', parse_mode='MarkdownV2',
                         reply_markup=await profile_button())


async def music(message: types.Message):
    random_music = random.choice(music_files)
    music_list = open(random_music, 'rb')
    await bot.send_message(chat_id=message.from_user.id, text='*Подождите пожалуйста, музыка грузится\.\.\.*',
                           parse_mode='MarkdownV2')
    await bot.send_audio(chat_id=message.from_user.id, audio=music_list, reply_markup=await save_music())


async def playlist(message: types.Message):
    pass


async def meme(message: types.Message):
    pass


def register_menu_handlers(dp: Dispatcher):
    dp.register_message_handler(menu, regexp=r'^Меню$')
    dp.register_message_handler(profile, regexp=r'^Профиль$')
    dp.register_message_handler(music, regexp=r'^Музыка$')
