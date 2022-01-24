class DequeElem:

    def __init__(self, data, prev_elem=None, next_elem=None):
        self.data = data
        self.prev_elem = prev_elem
        self.next_elem = next_elem


class Deque:

    def __init__(self):
        self.front = None
        self.back = None

    def view_back(self):
        if self.back is None:
            return None
        return self.back.data

    def view_front(self):
        if self.front is None:
            return None
        return self.front.data

    def push_back(self, data):
        if self.front == None and self.back == None:
            self.front = self.back = DequeElem(data)
        elem = DequeElem(data, prev_elem=self.back)
        self.back = elem

    def push_front(self, data):
        if self.front == None and self.back == None:
            self.front = self.back = DequeElem(data)
        elem = DequeElem(data, next_elem=self.front)
        self.front = elem

    def pop_back(self):
        if self.back is None:
            return None
        elem = self.back
        self.back = elem.prev_elem
        return elem.data

    def pop_front(self):
        if self.front is None:
            return None
        elem = self.front
        self.front = elem.next_elem
        return elem.data
