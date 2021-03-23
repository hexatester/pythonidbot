from telegram import Update
from telegram.ext import CallbackContext, InlineQueryHandler
from .hints import Hints


HINTS = Hints()


def inline_handler(update: Update, context: CallbackContext):
    if not update.inline_query:
        return
    inline_query = update.inline_query
    articles = list()
    if len(inline_query.query) < 4:
        return inline_query.answer(
            HINTS.hints_article,
            switch_pm_parameter="inline-help",
            switch_pm_text="Bantuan",
        )
    articles.extend(HINTS.find(inline_query.query))
    if not articles:
        articles.extend(HINTS.hints_article)
    inline_query.answer(
        articles,
        switch_pm_parameter="inline-help",
        switch_pm_text="Bantuan",
    )
    return


HANDLERS = []
HANDLERS.append(InlineQueryHandler(HINTS.hashtag_handler, pattern=r"^#\S+"))
HANDLERS.append(InlineQueryHandler(inline_handler))


def register_inlines(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
