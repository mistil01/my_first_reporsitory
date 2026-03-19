Crypto Price Bot 🤖
A Telegram bot that shows real-time cryptocurrency prices using the Binance API.
Features

Get live prices for Bitcoin, Ethereum and Dogecoin
Prices are displayed in USDT
Simple keyboard interface — no commands needed

Supported Cryptocurrencies
NameTickerBitcoinBTCUSDTEthereumETHUSDTDogeDOGEUSDT
Tech Stack

Python 3.13
pyTelegramBotAPI
Binance API
python-dotenv

Setup

Clone the repository:

git clone https://github.com/yourusername/crypto-bot.git
cd crypto-bot

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root directory:

TOKEN=your_telegram_bot_token

Run the bot:

python script.py
Usage

Start the bot with /start
Choose a cryptocurrency from the keyboard
The bot will return the current price in USDT

Project Structure
├── script.py          # Main bot file
├── requirements.txt   # Dependencies
├── .env               # Secret tokens (not in git)
└── .gitignore