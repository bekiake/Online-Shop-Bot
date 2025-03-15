import os
import asyncio
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from app.handlers import router
from app.database.models import async_main


async def main():
    load_dotenv()
    await async_main()
    bot = Bot(token=os.getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
