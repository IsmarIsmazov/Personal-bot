from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_button import games_choice


async def games(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Выбирите игру которую хотите поиграть',
                           reply_markup=await games_choice())
    try:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    except Exception as e:
        print(f"Ошибка при удалении сообщения: {e}")


async def dice_game(call: types.CallbackQuery):
    dice = await bot.send_dice(chat_id=call.from_user.id, emoji='🎲')
    await bot.send_message(chat_id=call.from_user.id, text=f'Вам выпало: {dice.dice.value}')
    print(dice.dice.value)
    if dice.dice.value == 6:
        await bot.send_message(chat_id=call.from_user.id, text='*Вы выиграли\!*', parse_mode='MarkdownV2')


async def bowling_game(call: types.CallbackQuery):
    await bot.send_dice(chat_id=call.from_user.id, emoji='🎳')


async def football_game(call: types.CallbackQuery):
    await bot.send_dice(chat_id=call.from_user.id, emoji='⚽')


async def basketball_game(call: types.CallbackQuery):
    await bot.send_dice(chat_id=call.from_user.id, emoji='🏀')


async def darts_game(call: types.CallbackQuery):
    await bot.send_dice(chat_id=call.from_user.id, emoji='🎯')


async def jackpot_game(call: types.CallbackQuery):
    await bot.send_dice(chat_id=call.from_user.id, emoji='🎰')


def register_games_handler(dp: Dispatcher):
    dp.register_message_handler(games, regexp=r'^Игры$')
    dp.register_callback_query_handler(dice_game, lambda call: call.data == "dice_game_call")
    dp.register_callback_query_handler(bowling_game, lambda call: call.data == "bowling_game_call")
    dp.register_callback_query_handler(football_game, lambda call: call.data == "football_game_call")
    dp.register_callback_query_handler(basketball_game, lambda call: call.data == "basketball_game_call")
    dp.register_callback_query_handler(darts_game, lambda call: call.data == "darts_game_call")
    dp.register_callback_query_handler(jackpot_game, lambda call: call.data == "jackpot_game_call")
