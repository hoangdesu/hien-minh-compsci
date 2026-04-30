# Fibonacci

# 0 1 1 2 3 5 8 13 21 34 55 ...
# 1 2 3 4 5 6 7  8  9 10 11 ...

# How many Fibonacci numbers: 9
# 0 1 1 2 3 5 8 13 21


# 0 1 1 2 3 5
# f s n
#   f s n
#     f s n
#       f s n


# fibonacci = [0, 1]

# total_num = int(input('How many Fibonacci numbers: '))
# needed_num = total_num - len(fibonacci) # 2

# first = fibonacci[0]
# second = fibonacci[1]
# for i in range(needed_num):
#     next = first + second
#     fibonacci.append(next)
#     # đổi chỗ 2 biến first & second
#     first = second
#     second = next
    
# for num in fibonacci:
#     print(num, end=" ")

# print()


# ----

# import random

# random_nums = [random.randint(1, 100) for _ in range(10)]
# print(random_nums)

# Find max and min numbers
# Max: 92
# Min: 4



# ----

# Frequency
phones = ['iphone', 'samsung', 'iphone', 'xiaomi', 'samsung', 'oppo', 'iphone']

iphone: 3
samsung: 2
xiaomi: 1
oppo: 1

