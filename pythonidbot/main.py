import logging
import sys

from telegram import ParseMode
from telegram.ext import Updater, Defaults
from typing import List, Optional

from pythonidbot.config import BOT_TOKEN, PORT, APP_URL, DISABLED_LOGGER
from pythonidbot.handlers import register as register_handlers
from pythonidbot.taghints import register as register_taghints


def set_logging(debug: bool = False, disabled: Optional[List[str]] = None):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    disabled = disabled or DISABLED_LOGGER
    for name in disabled:
        _logger = logging.getLogger(name)
        _logger.setLevel(logging.INFO)


def main():
    set_logging(not bool(APP_URL))
    defaults = Defaults(
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True,
    )
    updater = Updater(
        token=BOT_TOKEN,
        defaults=defaults,
    )
    register_handlers(updater.dispatcher)
    register_taghints(updater.dispatcher)
    if PORT:
        # updater.bot.setWebhook(APP_URL + BOT_TOKEN)
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
            webhook_url=APP_URL + BOT_TOKEN,
        )
    else:
        updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    sys.exit(main())
