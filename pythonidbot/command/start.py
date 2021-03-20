from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
        "Hai. Aku bot yang mengumumkan aturan di python indonesia"
    )


START_HANDLERS = [CommandHandler("start", start)]
