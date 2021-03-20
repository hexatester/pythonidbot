import logging
import sys

from telegram.ext import Updater
from pythonidbot.config import BOT_TOKEN, PORT, APP_URL
from pythonidbot.handlers import register


def set_logging(debug: bool = False):
    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )


def main():
    set_logging(not bool(APP_URL))
    updater = Updater(BOT_TOKEN)
    register(updater.dispatcher)
    if PORT:
        updater.bot.setWebhook(APP_URL + BOT_TOKEN)
        updater.start_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=BOT_TOKEN,
        )
    else:
        updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    sys.exit(main())
