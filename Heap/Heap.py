import math


class Heap(object):
    def __init__(self, invariant):
        self.queue = []
        self.size = 0
        self.invariant = invariant

    def _append(self, key):
        """ append a new value in queue """
        """ Returns: The index at which the new value is appended """
        if len(self.queue) > self.size:#  There is still space left in queue
            self.queue[self.size] = key
        # No space left in queue
        self.queue.append(key)
        atIndex = self.size
        self.size += 1
        return atIndex

    def _left(self, parent):
        if parent > self.size or parent < 0:
            raise ValueError('parent should be a valid queue element')
        return 2*parent + 1

    def _right(self, parent):
        if parent > self.size or parent < 0:
            raise ValueError('parent should be a valid queue element')
        return 2*parent + 2

    def _parent(self, child):
        if child > self.size or child < 0:
            raise ValueError('child should be a valide queue element')
        return int(math.floor((child - 1) / 2))

    def _swap(self, in1, in2):
        temp = self.queue[in1]
        self.queue[in1] = self.queue[in2]
        self.queue[in2] = temp

    def _heapify(self, badIndex):
        l = self._left(badIndex)
        r = self._right(badIndex)
        target = None

        if l < self.size and (not self.invariant(self.queue[badIndex], self.queue[l])):
            target = l
        else:
            target = badIndex
        if r < self.size and (not self.invariant(self.queue[target], self.queue[r])):
            target = r

        if target is not badIndex:
            self._swap(badIndex, target)
            self._heapify(target)

    def build_heap(self, items):
        """ Build a heap from the given list of items """
        for key in items:
            self.insert(key)

    def destroy(self):
        """ Destroy the heap """
        self.queue = []
        self.size = 0

    def pop(self):
        """Returns the top most element and rebalance the tree"""
        if self.size is 0:
            print "Heap is empty"
            return
        # Swap the top most element with the last one
        self._swap(0, self.size - 1)
        poppedKey = self.queue[self.size - 1]
        # Reduce the size of the queue
        self.size -= 1
        # Rebalance
        self._heapify(0)
        return poppedKey

    def insert(self, key):
        """ Insert a new element in the heap """

        badIndex = self._append(key)
        # heap invariant might be violated at the new index
        while badIndex > 0 and not self.invariant(self.queue[self._parent(badIndex)], self.queue[badIndex]):
            self._swap(badIndex, self._parent(badIndex))
            badIndex = self._parent(badIndex)

    def print_heap(self):
        """ Prints the elements of heap """
        print self.queue[:self.size:]
