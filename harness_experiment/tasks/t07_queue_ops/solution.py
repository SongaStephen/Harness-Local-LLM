class BoundedQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self._items = []

    def enqueue(self, item):
        if len(self._items) >= self.capacity:
            raise OverflowError("queue is full")
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("queue is empty")
        return self._items.pop(0)

    def peek(self):
        if not self._items:
            raise IndexError("queue is empty")
        return self._items[0]

    def is_full(self):
        return len(self._items) >= self.capacity