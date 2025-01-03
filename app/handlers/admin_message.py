from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import app.keyboards.reply as rkb
import app.keyboards.builder as bkb
import app.keyboards.inline as ikb

from app.filters.admin_filter import AdminProtect

from app.database import get_main_text_by_text_id


admin = Router()


@admin.message(AdminProtect(), Command("admin"))
@admin.message(AdminProtect(), F.text == "Админ-панель")
async def admin_panel(message: Message):
    admin_panel = await get_main_text_by_text_id(3)
    await message.answer(f"{admin_panel[2]}",
                         reply_markup=ikb.admin_panel)