from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from uuid import uuid4
from utils.csv_utils import read_csv_data

async def inline_query_handler(update, context):
    query = update.inline_query.query
    if not query:
        await context.bot.answer_inline_query(update.inline_query.id, [])
        return

    file_path = r"C:\Users\ASUS\OneDrive\دسکتاپ\googleplaystore.csv"
    data = read_csv_data(file_path)

    filtered = data[data['App'].str.contains(query, case=False, na=False)]
    results = []

    for _, row in filtered.iterrows():
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Show 5 Reviews", callback_data=f"show_reviews:{row['App']}")]
        ])
        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=row['App'],
                input_message_content=InputTextMessageContent(
                    message_text=f"Title: {row['App']}\nRating: {row['Rating']}\n..."
                ),
                reply_markup=keyboard
            )
        )

    await context.bot.answer_inline_query(update.inline_query.id, results)