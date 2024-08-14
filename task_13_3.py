from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

path_to_key = __file__.rsplit('/', maxsplit=3)[0]
with open(f'{path_to_key}/Документы/aiogram_api_key', 'r') as key:
    api = key.read().splitlines()
bot = Bot(token=api[0])
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
