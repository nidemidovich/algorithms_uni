class Vertex:
    def __init__(self, num, value):
        self.num = num
        self.value = value
        self.visited = False

    def __str__(self):
        return f'Vertex number is {str(self.num)}. Value is {str(self.value)}'
