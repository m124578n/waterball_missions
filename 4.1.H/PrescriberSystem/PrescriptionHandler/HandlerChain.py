

class HandlerChain:
    def __init__(self):
        self.handler = None

    def set_next(self, handler):
        if self.handler is None:
            self.handler = handler
        else:
            self.handler.next = handler
