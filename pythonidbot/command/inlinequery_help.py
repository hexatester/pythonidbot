from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Filters


def inlinequery_help(update: Update, context: CallbackContext):
    text = (
        "Inline : <pre>#hint pesan</pre>\n"
        "Contoh #aturan mohon baca aturan group akan menjadi\n\n"
        "mohon baca aturan group akan menjadi\n"
        "Silahkan baca Aturan Group PythonID di https://pythonid.github.io/aturan.html\n\n"
        "Inline : Pencarian, awali inline dengan <pre>?</pre> untuk membuat pesan dengan link search engine"
    )
    update.effective_message.reply_text(text)


INLINEQUERY_HELP_HANDLER = [
    CommandHandler(
        "start", inlinequery_help, filters=Filters.regex(r"^/start inline-help$")
    )
]
