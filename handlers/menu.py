from aiogram import Router, F, types
from aiogram.filters.command import Command
from config import db
import sqlite3


menu_router = Router()
@menu_router.message(Command("menu"))
@menu_router.message(F.data == "menu")
async def show_shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Суши"),
            ],
            [
                types.KeyboardButton(text="Пицца")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию", reply_markup=kb)


categories = ("пицца", "суши")

@menu_router.message(F.text.lower().in_(categories))
async def show_meals(message: types.Message):
    category = message.text.capitalize()  # одно из genres
    meals = await db.fetch("""
            SELECT * FROM meals
            INNER JOIN categories ON meals.category_id = categories.id
            WHERE categories.name = ?
        """, (category,))
    await message.answer(f"Блюда из {category}")
    for meal in meals:
        photo = types.FSInputFile(meal['image'])
        await message.answer_photo(
            photo=photo,
            caption=f"{meal['name']} - {meal['price']} сом"
        )
