from aiogram import types


async def start(message: types.Message):

    await message.answer("Привет, спорим я отгадаю как тебя зовут?")

    await message.answer(message.from_user.first_name)

    await message.answer(message.from_user.last_name)

    await message.answer("Если я отгадал напиши мне что-нибудь")


async def echo(message: types.Message):

    await message.answer(message.text)







