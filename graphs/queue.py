class QueueElement:

    def __init__(self, data, prev_elem=None, next_elem=None):
        self.data = data
        self.prev_elem = prev_elem
        self.next_elem = next_elem


class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def push(self, data):
        elem = QueueElement(data)
        if self.front == None and self.back == None:
            self.front = self.back = elem
        else:
            self.back.next_elem = elem
            elem.prev_elem = self.back
            self.back = elem

    def pop(self) -> QueueElement:
        if self.front == None:
            return None
        elem = self.front
        self.front = elem.next_elem
        return elem

    @property
    def size(self):
        size = 0
        current = self.front
        while current != None:
            size += 1
            current = current.next_elem
        return size
