from Heap import Heap

class MaxPQ(Heap):
    def __init__(self, items = []):
        invariant = lambda parent, child:  parent >= child
        super(MaxPQ, self).__init__(invariant)
        super(MaxPQ, self).build_heap(items)

    def insert(self, key):
        super(MaxPQ, self).insert(key)
        return

    def destroy(self):
        super(MaxPQ, self).destroy()

    def get_maximum(self):
        maximum = super(MaxPQ, self).pop()
        return maximum

    def change_key(self, index, newKey):
        if index > self.size or index < 0:
            raise ValueError('Out of bound index')

        if newKey > self.queue[index]:
            self._increase_key(index, newKey)
        else:
            self.decrease_key(index, newKey)

    def _increase_key(self, index, newKey):
        self.queue[index] = newKey
        while index > 0 and self.queue[index] > self.queue[super(MaxPQ, self)._parent(index)]:
            super(MaxPQ, self)._swap(index, super(MaxPQ, self)._parent(index))
        return

    def _decrease_key(self, index, newKey):
        self.queue[index] = newKey
        super(MaxPQ, self)._heapify(index)
        return
