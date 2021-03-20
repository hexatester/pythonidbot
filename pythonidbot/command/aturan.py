from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler


aturan_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "Aturan Grup PythonID", url="https://pythonid.github.io/aturan.html"
            )
        ]
    ]
)


def aturan(update: Update, context: CallbackContext):
    """Send a message when the command /aturan is issued."""
    update.message.reply_text(
        "<b>Penting!</b>Wajib gunakan username dan foto profil (profile picture)"
        " agar nyaman saat disebut dan enak dipandang mata."
        '<a href="https://pythonid.github.io/aturan.html">KLIK UNTUK BACA ATURAN SELENGKAPNYA.</a>',
        disable_web_page_preview=False,
        reply_markup=aturan_markup,
    )


ATURAN_HANDLERS = [CommandHandler("aturan", aturan)]
