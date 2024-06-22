import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL, BUTTON_TEXT, GREETING_MESSAGE

# Initialize the bot with the token from config
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Define the start command handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Create an inline button with WebAppInfo using URL and text from config
    inline_button = InlineKeyboardButton(text=BUTTON_TEXT, web_app=WebAppInfo(url=WEBAPP_URL))
    inline_keyboard = InlineKeyboardMarkup().add(inline_button)

    # Send the message with the inline button, using the greeting from config
    await message.answer(GREETING_MESSAGE, reply_markup=inline_keyboard)

# Define the main function to start polling
async def main():
    # Start polling
    await dp.start_polling()

# Run the bot
if __name__ == "__main__":
    asyncio.run(main())