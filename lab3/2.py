class shape:
    def __init__(self):
        pass
    def area(self):
        return 0


class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2


Shape = shape()
print(Shape.area())


Square = square(int(input()))
print(Square.area())
