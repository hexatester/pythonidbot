HANDLERS = []


def register_inlines(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
