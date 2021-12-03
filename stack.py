class StackElem:

    def __init__(self, data, prev):
        self.data = data
        self.prev = prev


class StackClassic:

    def __init__(self):
        self.top = None

    def view(self):
        if self.top is None:
            return None
        return self.top.data

    def push(self, data):
        elem = StackElem(data, self.top)
        self.top = elem

    def pop(self):
        if self.top is None:
            return None
        elem = self.top
        self.top = elem.prevelem
        return elem.data

    def show(self):
        elem = self.top
        while elem is not None:
            print(elem.data)
            elem = elem.prevelem
