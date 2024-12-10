# 1
import random
x = random.randint(1, 10)
y = random.randint(1, 10)
x_1 = random.randint(1, 10)
y_1 = random.randint(1, 10)
x_2 = random.randint(1, 10)
y_2 = random.randint(1, 10)
print(x, y)
print(x_1, y_1)
print(x_2, y_2)


def less(x, y, x_1, y_1, x_2, y_2):
    return (x/y, x_1/y_1, x_2/y_2)


if y/x < y_1/x_1 and y/x < y_2/x_2:
    print(x, y)
    if y_1/x_1 < y/x and y_1/x_1 < y_2/x_2:
        print(x_1, y_1)
        if y_2/x_2 < y_1/x_1 and y_2/x_2 < y/x:
            print(y_2, x_2)
else:
    print('не найдено!')

# 2


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_binary_palindrome(n):
    binary_rep = bin(n)[2:]
    return binary_rep == binary_rep[::-1]


def find_prime_binary_palindromes(n):
    result = []
    for num in range(2, n + 1):
        if is_prime(num) and is_binary_palindrome(num):
            result.append(num)
    return result


n = 100
primes_binary_palindromes = find_prime_binary_palindromes(n)
print(primes_binary_palindromes)
