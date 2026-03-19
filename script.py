from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import os
from dotenv import load_dotenv

load_dotenv()



TELEGRAM_TOKEN = os.getenv("TOKEN")
CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCUSDT",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGEUSDT"
}

bot = TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = ReplyKeyboardMarkup(row_width=3)
    for cripto_name in CRYPTO_NAME_TO_TICKER.keys():
        item_buttom = KeyboardButton(cripto_name)
        markup.add(item_buttom)
    bot.send_message(message.chat.id, text ="Choose a cripto",reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in CRYPTO_NAME_TO_TICKER.keys())
def send_price(message):
    cripto_name = message.text
    ticker = CRYPTO_NAME_TO_TICKER[cripto_name]
    price = get_price_by_ticker(ticker = ticker)
    bot.send_message(message.chat.id, text= f"price of {cripto_name} to USDT is {price}")

def get_price_by_ticker(*, ticker: str) -> float:
    endpoint = "https://api.binance.com/api/v3/ticker/price"
    params = {
        'symbol': ticker,
    }
    response = requests.get(endpoint, params=params)
    data = response.json()
    price = round(float(data["price"]), 2)
    return price
bot.infinity_polling()