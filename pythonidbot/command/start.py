#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
from telegram.ext import CommandHandler


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text("Selamat datang", disable_web_page_preview=True)


START_HANDLERS = [CommandHandler("start", start)]
