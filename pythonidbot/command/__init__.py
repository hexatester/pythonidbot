from .start import START_HANDLERS
from .aturan import ATURAN_HANDLERS


HANDLERS = []
HANDLERS.extend(ATURAN_HANDLERS)
HANDLERS.extend(START_HANDLERS)


def register_commands(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
