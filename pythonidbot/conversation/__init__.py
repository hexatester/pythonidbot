HANDLERS = []


def register_conversations(dispatcher):
    for handler in HANDLERS:
        dispatcher.add_handler(handler)
