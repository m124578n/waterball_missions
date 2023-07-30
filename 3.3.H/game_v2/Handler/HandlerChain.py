from .CollisionHandler import CollisionHandler



class HandlerChain:
    def __init__(self):
        self.handler = None

    def set_next(self, handler: CollisionHandler):
        if self.handler is None:
            self.handler = handler
        else:
            self.handler.next = handler

    def collision(self):
        return self.handler.collision()