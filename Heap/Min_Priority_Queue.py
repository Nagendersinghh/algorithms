from Heap import Heap

class MinPQ(Heap):
    def __init__(self, items = []):
        invariant = lambda parent, child: parent <= child
        super(MinPQ, self).__init__(invariant)
        super(MinPQ, self).build_heap(items)
        return

    def insert(self, key):
        super(MinPQ, self).insert(key)
        return

    def destroy(self):
        super(MinPQ, self).destroy()
        return

    def get_minimum(self):
        minimum = super(MinPQ, self).pop()
        return minimum

    def change_key(self, index, newKey):
        if index > self.size or index < 0:
            raise ValueError('Out of bound index')

        if newKey < self.queue[index]:
            self._decrease_key(index, newKey)
        else:
            self._increase_key(index, newKey)
        return

    def _increase_key(self, index, newKey):
        self.queue[index] = newKey
        super(MinPQ, self)._heapify(index)
        return

    def _decrease_key(self, index, newKey):
        self.queue[index] = newKey
        while index > 0 and self.queue[index] < self.queue[super(MinPQ, self)._parent(index)]:
            super(MinPQ, self)._swap(index, super(MinPQ, self)._parent(index))
        return
