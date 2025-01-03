from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import app.keyboards.reply as rkb
import app.keyboards.builder as bkb
import app.keyboards.inline as ikb

from app.filters.admin_filter import AdminProtect

from app.database import insert_user, get_main_text_by_text_id

user = Router()


@user.message(CommandStart())
async def start_command(message: Message):
    start_text = await get_main_text_by_text_id(1)
    start_admin = await get_main_text_by_text_id(2)
    admin = AdminProtect()
    if not await admin(message):  # Добавляем await здесь
        await message.answer(f"{start_text[2]}")
        await insert_user(message.from_user.id, message.from_user.username)
    else:
        await message.answer(f"{start_text[2]}")
        await insert_user(message.from_user.id, message.from_user.username)
        await message.answer(f"{start_admin[2]}",
                             reply_markup=rkb.admin_menu)