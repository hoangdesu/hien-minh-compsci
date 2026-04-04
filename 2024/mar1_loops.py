# for vs while

# Totalling: tinh tong

# array of integers
# numbers = [1, 2, 3]
# 1 + 2 + 3 = 6

# total = numbers[0] + numbers[1] + numbers[2]
# print(total)

# length of the array

# total = 0

# for i in range(len(numbers)):
#     total = total + numbers[i]
    

# print('total = ' + str(total))


# (1 + 2) + 3 + 4
# (3 + 3) + 4
# 6 + 4
# 10


# Counting
# array of string
# food = ['com chay', 'gao lut', 'banh', 'pho', 'bun rieu']

# # đếm số phần tử ở trong 1 chuỗi
# # print(len(food))

# count = 0
# for i in range(len(food)):
#     count = count + 1 # update count len 1 sau moi phan tu
    
# print('count: ' + str(count))

# HW:
nums = []
total = 0

counter = ['first', 'second', 'third']

for i in range(3):
    num = int(input('Enter ' + counter[i] + ' number: '))
    nums.append(num)
    
for i in range(len(nums)):
    total += num
    print(nums[i], end=" + ")
    
print('Total of the last 3 numbers:', total)

# 9 + 5 + 2 = 16