import logging
from fuzzywuzzy import process
from telegram import Update, InlineQueryResultArticle, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from typing import List, Optional

from pythonidbot.constants import HINTS
from pythonidbot.utils.helpers import article, build_menu


class Hints:
    def __init__(self, hints: Optional[List[dict]] = None):
        self.logger = logging.getLogger(__name__)
        self.hints = hints or list(HINTS.values())
        self.hints_article = [self.article(hint) for hint in self.hints]
        self.hints_q_dict = dict(enumerate([hint["help"] for hint in self.hints]))

    def __call__(
        self,
        query: str,
        limit: int = 10,
        score_cutoff: int = 60,
    ) -> List[InlineQueryResultArticle]:
        return self.find(query, limit, score_cutoff)

    def find(
        self,
        query: str,
        limit: int = 10,
        score_cutoff: int = 60,
    ) -> List[InlineQueryResultArticle]:
        self.logger.debug(f"Mencari hint dengan keyword `{query}`")
        best_hints = process.extractBests(
            query=query,
            choices=self.hints_q_dict,
            score_cutoff=score_cutoff,
            limit=limit,
        )
        self.logger.debug(f"Ditemukan {len(best_hints)} kemungkinan hint")
        return [self.hints_article[z] for (x, y, z) in best_hints] if best_hints else []

    def article(
        self,
        data: dict,
        query: Optional[str] = None,
        markup: Optional[InlineKeyboardMarkup] = None,
    ) -> InlineQueryResultArticle:
        message: str = data["message"]
        if "{query}" in message:
            query = query or data["default"]
            message = message.replace("{query}", query)
        if "buttons" in data:
            markup = self.make_button(data["buttons"])
        return article(
            title=data["help"],
            description=message,
            message_text=message,
            reply_markup=markup,
        )

    def make_button(self, buttons: List[dict]) -> InlineKeyboardMarkup:
        keyboards: List[InlineKeyboardButton] = list()
        for data in buttons:
            keyboards.append(InlineKeyboardButton(**data))
        menu = build_menu(keyboards, 1)
        return InlineKeyboardMarkup(menu)
