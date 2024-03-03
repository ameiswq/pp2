import re

#1
print(re.search(r"ab*", input("1:\n")))

#2
print(re.search(r"ab{2,3}[^b]", input("2:\n"))) # only 2 or 3 'b'

#3
print(re.search(r"[a-z]+_[a-z]+", input("3:\n")))

#4
print(re.search(r"[A-Z][a-z]+", input("4:\n")))

#5
print(re.search(r"a\S*b\b", input("5:\n")))

#6
print(re.sub(r"[ ,.]", ":", input("6:\n")))

#7 
s = input("7:\n")
arr = re.split(r"_", s)
s = ""
s += arr[0]
for x in arr[1:]:
    s+=x.capitalize()
print(s)


#8
print(*re.split(r"[A-Z]", input("8:\n")))

#9

string = input("9:\n")
a = re.findall(r"[A-Z][a-z]*", string)
string = ""
for x in a:
    string += x
    string += " "
print(string)

#10 
c = input("10:\n")
b = re.findall(r"^[a-z]+|[A-Z][a-z]*", c)
c = ""
print(*b)
for x in b:
    c += x.lower()
    c += " "
c = c[:len(c) - 1]
print(re.sub(r" ", "_", c))