from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()


#FSM Finite State Machine
class Recall(StatesGroup):
    name = State() #состояние связанное с именем пользователя
    contact = State()
    vizit_data = State()
    rate_dish = State()
    rate_cleanles = State()
    comments = State()

@survey_router.message(Command("survey"))
async def start_survey(message: types.Message, state: FSMContext):
    #устанавливаем состояние
    await state.set_state(Recall.name)
    await message.answer("Whats your name?")


#обработчик для остановки опроса
@survey_router.message(Command("stop"))
@survey_router.message(F.text == "stop")
async def stop_survey(message: types.Message, state: FSMContext):
    #очищаем все данные после остановки опроса
    await state.clear()
    await message.answer("Survey is stoped successfully")


@survey_router.message(Recall.name)
async def process_name(message: types.Message, state: FSMContext):
    print("Message", message.text)
    #устанавливая состояние
    await state.update_data(name=message.text)
    await state.set_state(Recall.contact)
    await message.answer("Give us ur contact number or social media")


@survey_router.message(Recall.contact)
async def process_contact(message: types.Message, state: FSMContext):
    print("Message", message.text)
    await state.update_data(contact=message.text)
    await state.set_state(Recall.vizit_data)
    await message.answer("When u were vizit our restourant last time?")


@survey_router.message(Recall.vizit_data)
async def process_vizit_data(message: types.Message, state: FSMContext):
    await state.update_data(vizit_data=message.text)
    await state.set_state(Recall.rate_dish)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Very nice", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Good", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Not bad", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Bad", callback_data="Thanks for Rating!")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Please rate our dishes {message.from_user.first_name}!", reply_markup=kb)


@survey_router.message(Recall.rate_dish)
async def process_rate_dish(message: types.Message, state: FSMContext):
    print("Message", message.text)
    await state.update_data(rata_dish=message.text)
    await state.set_state(Recall.rate_cleanles)
    kb = types.ReplyKeyboardRemove()
    await message.answer("Please rate our restourant cleanless", reply_markup=kb)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Very nice", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Good", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Not bad", callback_data="Thanks for Rating!")
            ],
            [
                types.KeyboardButton(text="Bad", callback_data="Thanks for Rating!")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer(f"Please rate our cleanless {message.from_user.first_name}!", reply_markup=kb)


@survey_router.message(Recall.rate_cleanles)
async def process_rate_cleanles(message: types.Message, state: FSMContext):
    print("Message", message.text)
    await state.update_data(rata_dish=message.text)
    await state.set_state(Recall.comments)
    kb = types.ReplyKeyboardRemove()
    await message.answer("Write some comments here!", reply_markup=kb)


@survey_router.message(Recall.comments)
async def process_rate_cleanles(message: types.Message, state: FSMContext):
    print("Message", message.text)
    await state.update_data(rate_cleanles=message.text)
    #сохранение в бд
    data = await state.get_data()
    print("Data", data)
    #чистим данные
    await state.clear()
    await message.answer("Thanks for Rateing our resturant")

