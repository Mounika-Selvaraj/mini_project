from typing import Final
import requests
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Constants
TOKEN: Final = '7442107225:AAFxUJBJGT9fRRV9SCgsQf8_hgvxqWL_ZOM'  # Replace with your bot token
OPENWEATHER_API_KEY: Final = 'b8562264114252a845e3b7c88d222393'  # Replace with your OpenWeatherMap API key

# Start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a Weather Bot! Type your city name to get weather updates.')

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Type your city name, and I will provide you with the weather information.')

# Function to fetch weather data
def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']
        min_temp = main['temp_min']
        max_temp = main['temp_max']
        pressure = main['pressure']
        humidity = main['humidity']
        wind_speed = data['wind']['speed']
        sunrise = time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunrise']))
        sunset = time.strftime("%I:%M:%S", time.gmtime(data['sys']['sunset']))

        return (f"Weather in {city.title()}:\n"
                f"Temperature: {temperature}°C\n"
                f"Min Temperature: {min_temp}°C\n"
                f"Max Temperature: {max_temp}°C\n"
                f"Pressure: {pressure} hPa\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s\n"
                f"Condition: {weather_description.capitalize()}\n"
                f"Sunrise: {sunrise}\n"
                f"Sunset: {sunset}.")
    else:
        return "I couldn't find that city. Please make sure you typed it correctly."

# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text
    weather_info = get_weather(city)
    await update.message.reply_text(weather_info)

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

# Main function
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print('Polling...')
    app.run_polling(poll_interval=3)
