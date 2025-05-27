import logging
from telegram.ext import ApplicationBuilder, CommandHandler, InlineQueryHandler, CallbackQueryHandler
from config import TOKEN
from handlers.command_handlers import *
from handlers.inline_handler import inline_query_handler
from handlers.callback_handler import button_handler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("time", time_handler))
    app.add_handler(CommandHandler("date", date_handler))
    app.add_handler(CommandHandler("fact", fact_handler))
    app.add_handler(CommandHandler("joke", joke_handler))
    app.add_handler(InlineQueryHandler(inline_query_handler))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()