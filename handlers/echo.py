from aiogram import Router, types
from aiogram.filters import Command


echo_router = Router()


@echo_router.message()
async def echo_handler(message: types.Message):
    await message.answer("Sorry, I didnt understand you")