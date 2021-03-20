HANDLERS = []


def register_callbacks(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
