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
