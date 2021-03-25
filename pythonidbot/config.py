import os

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    if "BOT_TOKEN" not in os.environ:
        print("Please install python-dotenv (pip install python-dotenv).")
        print("Then create .env file inside root project folder (like .gitignore),")
        print("Add line `BOT_TOKEN=<token from @botfather>` to .env")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PORT = os.environ.get("PORT")
APP_URL = os.environ.get("APP_URL")
DISABLED_LOGGER = ["telegram.bot", "telegram.ext.dispatcher"]
