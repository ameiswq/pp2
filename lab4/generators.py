#1
def squares(n):
    for i in range(n + 1):
        yield i**2

n = int(input())
s = squares(n)
next(s)
for i in range(1, n + 1):
    print(next(s), end=" ")
print()

#2

def even(d):
    for i in range(0, d + 1, 2):
        yield i

m = int(input())
e = even(m)
for i in range(0, m + 1, 2):
    k = next(e) 
    if k == m or k == m - 1:
        print(k)
    else:
        print(k, end=", ")

#3
def check(z):
    for i in range(0, z + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
d = int(input())
c = check(d)
for i in c:
    print(i, end=" ")
print()

#4
def Square(a, b):
    for i in range(a, b + 1):
        yield i**2
a, b = map(int, input().split())
p = Square(a, b)
for i in p:
    print(i, end=" ")
print()


#5
def rev(n):
    for i in range(n, -1, -1):
        yield i
q = int(input())
r = rev(q)
for i in r:
    print(i, end=" ")