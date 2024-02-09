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

    def dist(point1, point2):
        return sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)


x, y = map(int, input().split())
point1 = Point(x, y)
a, b = map(int, input().split())
point2 = Point(a, b)

k = True
while k:
    s = input()
    if s == "show p1":
        point1.show()
    elif s == "show p2":
        point2.show()
    elif s == "move p1":
        w, q = map(int, input().split())
        point1.move(w, q)
    elif s == "move p2":
        w, q = map(int, input().split())
        point2.move(w, q)
    elif s == "dist":
        print(point1.dist(point2))
    else:
        k = False
    