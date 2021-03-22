from telegram import Update
from telegram.ext import CallbackContext, CommandHandler


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    if update.effective_user:
        name = update.effective_user.full_name
        update.message.reply_text(f"Selamat datang {name}!")
    else:
        update.message.reply_text(f"Hai!")


START_HANDLERS = [CommandHandler("start", start)]
