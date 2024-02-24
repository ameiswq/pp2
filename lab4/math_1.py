import math

#1
print(math.radians(float(input())))

#2
print("The area:", float(0.5*(int(input("Base, first value: ")) + int(input("Base, second value: "))))*int(input("Height: ")))
#3
n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))
print("The area of the polygon is:", 0.25 * n * (a**2) * (1/math.tan(math.radians(180/n))))

#4
print("The area of a parallelogram:", float(int(input("Length of base: ")) * int(input("Height of parallelogram:"))))