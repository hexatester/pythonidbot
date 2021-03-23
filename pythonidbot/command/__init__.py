from .start import START_HANDLERS
from .aturan import ATURAN_HANDLERS
from .inlinequery_help import INLINEQUERY_HELP_HANDLER


HANDLERS = []
HANDLERS.extend(ATURAN_HANDLERS)
HANDLERS.extend(INLINEQUERY_HELP_HANDLER)
HANDLERS.extend(START_HANDLERS)


def register_commands(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
