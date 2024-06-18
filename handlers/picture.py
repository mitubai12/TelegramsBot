from aiogram import Router, types
from aiogram.filters import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInputFile("img/stolas.jpg")
    await message.answer_photo(photo=file, caption=f'cat')

