from aiogram.utils import executor
from config import dp
import logging

from handlers import start, menu

menu.register_menu_handlers(dp=dp)
start.register_start_handlers(dp=dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
