class Stack:
    def __init__(self):
        self.items = []
        self.items_q = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def stack_to_queue(self):
        a = self.items
        a.reverse()
        self.items_q = [i for i in a]
        return self.items_q

