class Queue:
    def __init__(self):
        self.items = []
        self.items_s = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def queue_to_stack(self):
        a = self.items
        a.reverse()
        self.items_s = [i for i in a]
        return self.items_s