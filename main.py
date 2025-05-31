import logging
import pandas as pd
import requests
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    InlineQueryHandler,
    CallbackQueryHandler
)
from uuid import uuid4
from datetime import datetime
from persiantools.jdatetime import JalaliDate 

# ------------------------- Logging -------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ------------------------- Bot Token -------------------------
TOKEN = "your-token-goes-here"

# ------------------------- Help Message -------------------------
HELP_COMMAND_RESPONSE = """
👋 Welcome! Here's how you can interact with this bot:

🔹 /start - Start chatting with the bot  
🔹 /time - Get the current time  
🔹 /fact - Receive an interesting random fact  
🔹 /joke - Get a random funny joke 😂  
🔹 /date - See today’s date in the Persian (Jalali) calendar  
🔹 /help - View this help message again

🔍 You can also use this bot inline by typing @Googleplay_review_bot <app name> in any chat to search for app details and user reviews from Google Play.

If you have any questions or need help, just reach out. Enjoy using the bot! 😊
"""

# ------------------------- CSV Reader -------------------------
def read_csv_data(file_path, encoding='utf-8'):
    try:
        data = pd.read_csv(file_path, encoding=encoding)
        return data
    except Exception as e:
        logger.error(f"Error reading CSV file: {e}")
        return pd.DataFrame()

# ------------------------- Handlers -------------------------
async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Dear {update.effective_user.username}, welcome to our robot! /help"
    )

async def time_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=current_time,
        reply_to_message_id=update.effective_message.id
    )

async def fact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        fact = data.json()["text"]
    except Exception as e:
        logger.error(f"Error fetching fact: {e}")
        fact = "❌ Couldn't fetch a fact at the moment."
    await context.bot.send_message(chat_id=update.effective_chat.id, text=fact)

async def joke_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke = response.json()
        joke_text = f"😂 {joke['setup']}\n\n{joke['punchline']}"
    except Exception as e:
        logger.error(f"Error fetching joke: {e}")
        joke_text = "❌ Couldn't fetch a jokes at the moment.م"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=joke_text)

async def date_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = JalaliDate.today()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f" تاریخ شمسی امروز:\n{today.strftime('%Y/%m/%d')}",
        reply_to_message_id=update.effective_message.id
    )

async def help_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=HELP_COMMAND_RESPONSE,
        reply_to_message_id=update.effective_message.id
    )

def get_reviews_for_app(reviews_data, app_name, num_reviews=5):
    filtered_reviews = reviews_data[reviews_data['App'] == app_name]
    return filtered_reviews.head(num_reviews)

def format_reviews(reviews):
    if reviews.empty:
        return "No reviews found for this application."

    review_messages = []
    counter = 1
    for index, row in reviews.iterrows():
        review_messages.append(f"Review {counter}:\n{row['Translated_Review']}\nSentiment: {row['Sentiment']}\n")
        counter += 1

    return "\n".join(review_messages)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    app_name = query.data.split(":")[1]

    reviews_file_path = r"C:\Users\ASUS\OneDrive\دسکتاپ\googleplaystore_user_reviews.csv"
    reviews_data = read_csv_data(reviews_file_path, encoding='utf-8')
    reviews = get_reviews_for_app(reviews_data, app_name)
    formatted_reviews = format_reviews(reviews)

    await context.bot.send_message(chat_id=query.from_user.id, text=formatted_reviews)

async def inline_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    logger.info(f"Received inline query: {query}")
    if not query:
        await context.bot.answer_inline_query(update.inline_query.id, [])
        return

    file_path = r"C:\Users\ASUS\OneDrive\دسکتاپ\googleplaystore.csv"
    data = read_csv_data(file_path, encoding='utf-8')

    if data.empty:
        logger.error("No data found in the CSV file.")
        await context.bot.answer_inline_query(update.inline_query.id, [])
        return

    results = []
    filtered_data = data[data['App'].str.contains(query, case=False, na=False)]

    if filtered_data.empty:
        await context.bot.answer_inline_query(update.inline_query.id, [])
        return

    for index, row in filtered_data.iterrows():
        keyboard = [
            [InlineKeyboardButton("Show 5Reviews", callback_data=f"show_reviews:{row['App']}")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=row['App'],
                input_message_content=InputTextMessageContent(
                    message_text=f"Title: {row['App']}\n"
                                 f"Rating: {row['Rating']}\n"
                                 f"Category: {row['Category']}\n"
                                 f"Number of Reviews: {row['Reviews']}\n"
                                 f"Size: {row['Size']}\n"
                                 f"Installs: {row['Installs']}\n"
                                 f"Type: {row['Type']}\n"
                                 f"Price: {row['Price']}\n"
                                 f"Content Rating: {row['Content Rating']}\n"
                                 f"Genres: {row['Genres']}\n"
                                 f"Last Updated: {row['Last Updated']}\n"
                                 f"Current Version: {row['Current Ver']}\n"
                                 f"Android Version: {row['Android Ver']}\n"
                ),
                description=f"Rating: {row['Rating']}, Category: {row['Category']}, Number of Reviews: {row['Reviews']}",
                reply_markup=reply_markup
            )
        )
    await context.bot.answer_inline_query(update.inline_query.id, results)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Error: {context.error} on Update {update}")

# ------------------------- Main Entry -------------------------
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start_handler))
    application.add_handler(CommandHandler("help", help_command_handler))
    application.add_handler(CommandHandler("time", time_command_handler))
    application.add_handler(CommandHandler("fact", fact_handler))
    application.add_handler(CommandHandler("joke", joke_handler))  # <--- New joke handler
    application.add_handler(CommandHandler("date", date_command_handler))
    application.add_handler(InlineQueryHandler(inline_query_handler))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_error_handler(error_handler)

    application.run_polling()
