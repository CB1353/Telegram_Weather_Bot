import telebot
import requests

bot = telebot.TeleBot("")


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Hi there! I'm Cristian's friendly Telegram bot. "
                          "I can tell you the weather characteristics "
                          "in any city you type. Just type the name of the city you want to know more about!")


@bot.message_handler(func=lambda msg: msg.text is not None)
def get_weather(message):
    url = 'https://api.weatherbit.io/v2.0/current_key = d4d412cd9eb34dd4965368d3e66f7db3'
    city = message.text
    res = requests.get(url + format(city))
    data = res.json()
    temp = data['data'][0]['temp']
    wind_speed = data['data'][0]['wind_spd']
    humidity = data['data'][0]['rh']
    bot.reply_to(message, "The current temperature in {} is {} degrees Celsius. "
                          "The average wind speed is {} km/h and the humidity is {}%."
                 .format(city, temp, wind_speed, humidity))


bot.polling()
