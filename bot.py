import asyncio
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import BOT_TOKEN, WEBAPP_URL, BUTTON_TEXT, GREETING_MESSAGE, SECOND_BUTTON_TEXT, SECOND_BUTTON_URL

# Initialize the bot with the token from config
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


# Define the start command handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Create an inline button with WebAppInfo using URL and text from config
    webapp_button = InlineKeyboardButton(text=BUTTON_TEXT, web_app=WebAppInfo(url=WEBAPP_URL))

    # Create a new button for the second link using config values
    second_button = InlineKeyboardButton(text=SECOND_BUTTON_TEXT, url=SECOND_BUTTON_URL)

    # Create an inline keyboard and add both buttons
    inline_keyboard = InlineKeyboardMarkup().add(webapp_button).add(second_button)

    # Send the message with the inline buttons, using the greeting from config
    await message.answer(GREETING_MESSAGE, reply_markup=inline_keyboard)


# Define the main function to start polling
async def main():
    # Start polling
    await dp.start_polling()


# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
