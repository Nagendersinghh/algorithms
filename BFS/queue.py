class queue():
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return True if len(self.queue) == 0 else False

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            raise ValueError('Underflow')
        return self.queue.pop(0)
