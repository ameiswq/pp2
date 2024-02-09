from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def show(self):
        print(self.x, self.y)

    def move(self, nx, ny):
        self.x = nx
        self.y = ny 

    def dist(self, point2):
        return sqrt((self.x - point2.x)**2 + (self.y - point2.y)**2)


x, y = map(int, input().split())
point1 = Point(x, y)
a, b = map(int, input().split())
point2 = Point(a, b)

point1.show()
point2.show()

p,d = map(int, input().split())
point1.move(p, d)
print(point1.dist(point2))