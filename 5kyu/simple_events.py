class Event():
    def __init__(self):
        self.handlers = []
        
    def subscribe(self, f):
        self.handlers.append(f)
        
    def unsubscribe(self, f):
        self.handlers.remove(f)
        
    def emit(self, *args, **kwargs):
        for e in self.handlers:
            e(*args, **kwargs)