from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Shop", callback_data="shop")],
        [InlineKeyboardButton(text="🛍 Cart", callback_data="cart")],
        [InlineKeyboardButton(text="📦 Orders", callback_data="orders")],
        [InlineKeyboardButton(text="🛠 Settings", callback_data="settings")],
        [InlineKeyboardButton(text="📞 Contact", callback_data="contact")],
    ]
)