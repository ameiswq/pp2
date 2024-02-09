#1
def GramsToOunces(grams):
    print(28.3495231 * grams)
GramsToOunces(float(input()))


#2
def FahrenheitToCentigrade(n):
    print((5/9)*(n - 32))
FahrenheitToCentigrade(float(input()))


#3
def solve(heads, legs):
    for i in range(heads + 1):
        if i * 2 + (heads - i) * 4 == legs:
            print(i, "chickens and", heads - i, "rabbits")
solve(int(input()), int(input()))


#4
def filter_prime(arr):
    for x in arr:
        k = True
        if x <= 1:
            k = False
        else:
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    k = False
        if k:
            print(x, end=" ")
filter_prime(list(map(int, input().split())))


#5
from itertools import permutations
def Permutations(string):
    perm = permutations(string)
    for i in list(perm):
        print (''.join(i))
Permutations(input())


#6
def Reverse(arr):
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")
Reverse(list(input().split()))

#7
def check(arr):
    for i in range(len(arr) - 1):
        if arr[i] == 3 and arr[i + 1] == 3:
            print("True")
            return True
    print("False")
    return False
check(list(map(int, input().split())))


#8
def check(arr):
    a = []
    for x in arr:
        if x == 0 or x == 7:
            a.append(x)
    if len(a) < 3:
        print("False")
        return False
    for i in range(len(a) - 2):
        if a[i] == 0 and a[i + 1] == 0 and a[i + 2] == 7:
            print("True")
            return True
    print("False")
    return False
check(list(map(int, input().split())))


#9
import math
def volume(r):
    print(float((4/3) * math.pi * r**3))
volume(float(input()))


#10
def check(arr):
    a = []
    for x in arr:
    	if x in a:
    		continue
    	else:
    		a.append(x)
    		print(x, end=" ")
check(list(map(int, input().split())))


#11
def check(string):
    s = string[::-1]
    if s == string:
        print("YES")
    else:
        print("NO")
check(input())


#12
def histogram(arr):
    for x in arr:
        for i in range(x):
            print("*", end="")
        print()
histogram(list(map(int, input().split())))


#13
import random
n = random.randint(1, 20)
s = input("Hello! What is your name? \n")
print("Well,", s, ", I am thinking of a number between 1 and 20.")

p = 0
while True:
    p += 1
    a = int(input("Take a guess. \n"))
    if a == n:
        print("Good job,", s, "! You guessed my number in", p, "guesses!")
        break
    elif a > n:
       print("Your guess is too high.")
    else:
        print("Your guess is too low.")
