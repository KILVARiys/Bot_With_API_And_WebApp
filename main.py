import asyncio
import aiohttp
import logging

from urllib.parse import quote
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

TOKEN = 'YOUR_TOKEN'
API_TOKEN = 'YOUR_TOKEN'

bot = Bot(token=TOKEN)
dp = Dispatcher()

class WeatherState(StatesGroup):
    waiting_city = State()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_name = message.from_user.first_name
    await message.answer(
        text=f'''
        Привет, {user_name}!
        Чтобы узнать новости о погоде введит /weather
        ''')

@dp.message(Command('weather'))
async def weather_command(message: types.Message, state: FSMContext):
    await message.answer('Введите название города')
    await state.set_state(WeatherState.waiting_city)

@dp.message(WeatherState.waiting_city)
async def get_city(message: types.Message, state: FSMContext):
    city = message.text
    weather_info_from_site = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_TOKEN}&units=metric&lang=ru'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(weather_info_from_site) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                content = data['weather'][0]['description']
                temp_real = data['main']['feels_like']
                wind = data['wind']['speed']
                
                encoded_city = quote(city)
                encoded_content = quote(content)
                
                web_app_url = f"https://kilvariys.github.io/Bot_With_API_And_WebApp/?city={encoded_city}&temp={temp}&desc={encoded_content}&feels={temp_real}&wind={wind}"
                
                keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [InlineKeyboardButton(
                            text="🌤 Посмотреть погоду в WebApp",
                            web_app=WebAppInfo(url=web_app_url)
                        )]
                    ]
                )
                
                await message.answer(
                    f'''
                        Погода в городе - {city}:
                        Температура - {temp}°C
                        Ощущается как - {temp_real}°C
                        Скорость ветра - {wind} м/с
                        Описание - {content}
                    ''',
                    reply_markup=keyboard
                )
            else:
                await message.answer('Город не найден. Попробуйте еще раз.')
    
    await state.clear()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())