import asyncio
import logging

from config import dp, bot
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.survey import survey_router
from handlers.menu import menu_router
from handlers.echo import echo_router
from config import dp, bot, db


async def on_startup(bot):
    await db.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(survey_router)
    dp.include_router(menu_router)
    dp.include_router(echo_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

