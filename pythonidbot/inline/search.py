from telegram import Update
from telegram.ext import CallbackContext
from urllib.parse import quote_plus

from pythonidbot.utils.helpers import article


class SearchInline:
    def __init__(self):
        super().__init__()

    def __call__(self, update: Update, context: CallbackContext):
        query = update.inline_query.query
        query = query.lstrip("?")
        results_list = self.query(query)
        update.inline_query.answer(
            results=results_list,
        )

    def query(self, query: str):
        quoted_query = quote_plus(query)
        return [
            self.inline_article(
                title="š¦ DuckDuckGo",
                description=f'Cari "{query}" via DuckDuckGo',
                message_text=f'Pencarian via š¦<i>DuckDuckGo?</i>\nš <a href="https://duckduckgo.com/?q={quoted_query}">{query}</a>',
                thumb_url="https://duckduckgo.com/assets/icons/meta/DDG-iOS-icon_152x152.png",
            ),
            self.inline_article(
                title="š StackOverflow",
                description=f'Cari "{query}" via StackOverflow',
                message_text=f'Pencarian via š<i>StackOverflow?</i>\nš <a href="https://stackoverflow.com/search?q={quoted_query}">{query}</a>',
                thumb_url="https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png",
            ),
            self.inline_article(
                title="š Google",
                description=f'Cari "{query}" via Google',
                message_text=f'Pencarian via š<i>Google?</i>\nš <a href="https://google.com/search?q={quoted_query}">{query}</a>',
                thumb_url="https://seeklogo.net/wp-content/uploads/2015/09/google-favicon-vector-400x400.png",
            ),
            self.inline_article(
                title="š GitHub",
                description=f'Cari "{query}" via StackOverflow',
                message_text=f'Pencarian via š<i>GitHub?</i>\nš <a href="https://github.com/search?q={quoted_query}">{query}</a>',
                thumb_url="https://github.com/fluidicon.png",
            ),
            self.inline_article(
                title="š WikipediA",
                description=f'Cari "{query}" via WikipediA',
                message_text=f'Pencarian via š<i>WikipediA?</i>\nš <a href="https://wikipedia.org/wiki/Special:Search?search={quoted_query}">{query}</a>',
                thumb_url="https://wikipedia.org/static/apple-touch/wikipedia.png",
            ),
            self.inline_article(
                title="š PyPi",
                description=f'Cari "{query}" via PyPi',
                message_text=f'Pencarian via š<i>PyPi?</i>\nš <a href="https://pypi.org/search/?q={quoted_query}">{query}</a>',
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/110px-Python-logo-notext.svg.png",
            ),
            self.inline_article(
                title="š½ Bing",
                description=f'Cari "{query}" via Bing',
                message_text=f'Pencarian via š½<i>Bing?</i>\nš <a href="https://bing.com/search?q={quoted_query}">{query}</a>',
                thumb_url="https://pbs.twimg.com/profile_images/688769847900033024/Zdfx4cj5_400x400.png",
            ),
            self.inline_article(
                title="šŗ YouTube",
                description=f'Cari "{query}" via YouTube',
                message_text=f'Pencarian via šŗ<i>YouTube?</i>\nš <a href="https://www.youtube.com/results?search_query={quoted_query}">{query}</a>',
                thumb_url="https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Youtube-logo-white.png/240px-Youtube-logo-white.png",
            ),
        ]

    inline_article = staticmethod(article)
