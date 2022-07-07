from aiogram import Bot, Dispatcher, executor, types
import handlers
import logging



API_TOKEN = "5483531071:AAHLi3MIpevkWYAzzVfw0oNcst1m7NIz-IM"

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



dp.register_message_handler(handlers.start, commands=["start"])

dp.register_message_handler(handlers.echo)


if __name__ == '__main__':
    
    executor.start_polling(dp, skip_updates=True)

