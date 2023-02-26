import telebot
import requests


API_KEY = ""
bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hi there! I'm Cristian's weather bot. "
                          "I can tell you the weather characteristics in any city you want. "
                          "Just type the name of the city you want to know more about!")


@bot.message_handler(func=lambda message: True)
def get_weather(message):
    city = message.text
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}"
    res = requests.get(url)
    if res.status_code != 200:
        bot.reply_to(message, f"Sorry, {city} isn't a city. Please enter a valid city name: ")
        return
    data = res.json()
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    if 'clear sky' in description.lower() or 'sunny' in description.lower():
        description = '☀️'
    elif 'broken clouds' in description.lower() or 'overcast clouds' in description.lower():
        description = '☁️'
    elif 'rain' in description.lower():
        description = '🌧'
    elif 'snow' in description.lower():
        description = '❄️'
    bot.reply_to(message, f"The current weather in {city} 🌆 is {description}. "
                          f"The 🌡 is {temp}°C (feels like {feels_like}°C), "
                          f"💧 is {humidity}%, and 🌬 is {wind_speed} m/s.")


bot.polling()
