"""Thank you https://github.com/python-telegram-bot/rules-bot/blob/master/components/taghints.py"""
from collections import namedtuple

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackContext

from pythonidbot.constants import HINTS
from pythonidbot.utils.helpers import build_menu


def list_available_hints(update: Update, context: CallbackContext):
    message = "Anda dapat menggunakan hashtag berikut untuk memandu anggota baru:\n\n"
    message += "\n".join(
        "🗣 {tag} ➖ {help}".format(tag=k, help=v["help"]) for k, v in HINTS.items()
    )
    message += "\n\nPastikan untuk membalas pesan lain, jadi saya tahu siapa yang harus dirujuk."
    update.effective_message.reply_text(
        message, parse_mode=ParseMode.HTML, disable_web_page_preview=True
    )


Hint = namedtuple("Hint", "help, msg, reply_markup")


def get_hints(query):
    results = {}
    hashtag, _, query = query.partition(" ")

    for k, v in sorted(HINTS.items()):
        if k.lower().startswith(hashtag.lower()):
            reply_markup = (
                InlineKeyboardMarkup(
                    build_menu(
                        [
                            InlineKeyboardButton(
                                **{k: v.format(query=query) for k, v in b.items()}
                            )
                            for b in v["buttons"]
                        ],
                        1,
                    )
                )
                if "buttons" in v
                else None
            )

            msg = v["message"].format(query=query if query else v.get("default", ""))

            results[k] = Hint(
                help=v.get("help", ""), msg=msg, reply_markup=reply_markup
            )

    return results


def hint_handler(update: Update, context: CallbackContext):
    reply_to = update.message.reply_to_message

    hint = get_hints(update.message.text).popitem()[1]

    if hint is not None:
        update.effective_message.reply_text(
            hint.msg,
            reply_markup=hint.reply_markup,
            reply_to_message_id=reply_to.message_id if reply_to else None,
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
        )
        try:
            update.effective_message.delete()
        except BadRequest:
            pass


def register(dispatcher):
    dispatcher.add_handler(
        MessageHandler(
            Filters.regex(rf'(?i){"|".join(HINTS.keys())}'),
            hint_handler,
            run_async=True,
        )
    )
    dispatcher.add_handler(
        CommandHandler(("hints", "listhints"), list_available_hints, run_async=True)
    )
