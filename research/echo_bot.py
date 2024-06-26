from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os 
import logging

load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# configure logging 

logging.basicConfig(level=logging.INFO)

# Initilizer bot 
bot = Bot(token= API_TOKEN) #botFather created 
dp = Dispatcher(bot)  # All handlers should be attached to the Router (or Dispatcher)

@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
            """"This handler receives messages with `/start` or `/help` command
            
            Args:
                    message (types.Message): _description_
            """
            await message.reply("Hi! \n I am an Echo bot!\n Powered by Aiogram")
            


@dp.message_handler()
async def echo(message: types.Message):
            """"This handler receives messages with `/start` or `/help` command
            
            Args:
                    message (types.Message): _description_
            """
            await message.reply(message.text)
            
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
