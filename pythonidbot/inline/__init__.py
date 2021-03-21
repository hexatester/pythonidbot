from telegram import Update
from telegram.ext import CallbackContext, InlineQueryHandler
from .hints import Hints


HINTS = Hints()


def inline_handler(update: Update, context: CallbackContext):
    if not update.inline_query or not update.inline_query.query:
        return
    if len(update.inline_query.query) < 3:
        update.inline_query.answer(HINTS.hints_article)
        return
    articles = list()
    articles.extend(HINTS.find(update.inline_query.query))
    if not articles:
        articles.extend(HINTS.hints_article)
    update.inline_query.answer(articles)
    return


HANDLERS = []
HANDLERS.append(InlineQueryHandler(inline_handler))


def register_inlines(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
