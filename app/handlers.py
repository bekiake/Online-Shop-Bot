from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from app import keyboards as kb
from app.database.requests import set_user
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await set_user(tg_id=message.from_user.id, name=message.from_user.full_name)
    await message.answer("Hello! Welcome to <b>Online Shop</b>!", reply_markup=kb.menu)
    