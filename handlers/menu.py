from aiogram import Router, F, types
from aiogram.filters.command import Command
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


@menu_router.message(F.text == "Пицца")
async def show_drama(message: types.Message):
    category = message.text
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM meals WHERE category_id = 2")
    meals = query.fetchall()
    await message.answer(f"Блюда из {category}")
    for meal in meals:
        # Assuming 'image' is the fourth column, index 3
        photo = types.FSInputFile(meal[3])
        await message.answer_photo(
            photo=photo,
            caption=f"{meal[1]} - {meal[2]} сом"  # name at index 1, price at index 2
        )


@menu_router.message(F.text == "Суши")
async def show_drama(message: types.Message):
    category = message.text
    connection = sqlite3.connect("db.sqlite3")
    cursor = connection.cursor()
    query = cursor.execute("SELECT * FROM meals WHERE category_id = 1")
    meals = query.fetchall()
    await message.answer(f"Блюад из {category}")
    for meal in meals:
        photo = types.FSInputFile(meal[3])
        await message.answer_photo(
            photo=photo,
            caption=f"{meal[1]} - {meal[2]} сом"
        )

