import math
def prime(n):
	
    if n <= 1:
    	return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True 

def not_prime(n):
	
    if n <= 1:
    	return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return True
    return False

arr = list(map(int, input().split())) 
a = arr
prime_numbers = list(filter(lambda x: prime(x), arr))
not_prime_numbers = list(filter(lambda x: not_prime(x), a))
print("Prime array:", *prime_numbers)
print("Not prime array:", *not_prime_numbers)