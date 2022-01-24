class StackElem:

    def __init__(self, data, prev):
        self.data = data
        self.prev = prev


class StackClassic:

    def __init__(self):
        self.top = None

    def view(self):
        if self.top == None:
            return None
        return self.top.data

    def push(self, data):
        elem = StackElem(data, self.top)
        self.top = elem

    def pop(self):
        if self.top == None:
            return None
        elem = self.top
        self.top = elem.prev
        return elem.data

    def show(self):
        elem = self.top
        while elem != None:
            print(elem.data)
            elem = elem.prev
