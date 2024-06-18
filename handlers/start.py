from aiogram import Router, types, F
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Our site", url="https://geeks.kg")
            ],
            [
                types.InlineKeyboardButton(text="Our Instagram", url="https://www.instagram")
            ],
            [
                types.InlineKeyboardButton(text="About us", callback_data="about")
            ]
        ]
    )
    await message.answer(f'hello {message.from_user.first_name}', reply_markup=kb)


@start_router.callback_query(F.data == "about")
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"Hello {callback.message.from_user.first_name} heres some info")


@start_router.callback_query(F.data == "donate")
async def callback_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f'{callback.message.from_user.first_name} donate us')

