from aiogram import types, Dispatcher
from config import bot, ADMINS
from keyboards.reply_button import start_button
from database.sql_commands import Database


async def start(message: types.Message):
    Database().sql_insert_telegram_users_command(telegram_id=message.from_user.id,
                                                 username=message.from_user.username)
    await message.answer(f'Добро пожаловать *{message.from_user.first_name}*',
                         parse_mode='MarkdownV2',
                         reply_markup=await start_button())


async def helps(message: types.Message):
    await message.answer('/start - начать пользоваться ботом\n'
                         'Профиль - просмотр своего профиля\n'
                         'Меню - основныем команды бота\n'
                         'Плейлист - музыки которые вы сохранили\n'
                         'Музыка - рандомная музка\n'
                         'Мем - рандомный мем')


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(helps, commands=['help'])
