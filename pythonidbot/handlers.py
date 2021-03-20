from telegram.ext import Dispatcher

from pythonidbot.callback import register_callbacks
from pythonidbot.command import register_commands
from pythonidbot.conversation import register_conversations
from pythonidbot.error import register_errors

REGISTERS = [
    register_errors,
    register_conversations,
    register_callbacks,
    register_commands,
]


def register(dispatcher: Dispatcher):
    for register in REGISTERS:
        register(dispatcher)
