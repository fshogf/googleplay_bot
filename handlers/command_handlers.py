from datetime import datetime
from persiantools.jdatetime import JalaliDate
import requests
from telegram import Update
from telegram.ext import ContextTypes
from utils.messages import HELP_COMMAND_RESPONSE

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Dear {update.effective_user.username}, welcome to our robot! /help")

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_COMMAND_RESPONSE)

async def time_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update.message.reply_text(now)

async def date_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = JalaliDate.today().strftime('%Y/%m/%d')
    await update.message.reply_text(f"تاریخ شمسی امروز:\n{today}")

async def fact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        res = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        fact = res.json()["text"]
    except:
        fact = "❌ Couldn't fetch a fact right now."
    await update.message.reply_text(fact)

async def joke_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        res = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = res.json()
        text = f"😂 {joke['setup']}\n\n{joke['punchline']}"
    except:
        text = "❌ Couldn't fetch a joke."
    await update.message.reply_text(text)