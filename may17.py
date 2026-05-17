nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# search_num = int(input('Enter search num: '))
def binary_search(nums, search_num):
    low = 0
    high = len(nums) - 1

    found = False
    while low <= high:
        mid = (low + high) // 2
        
        if search_num == nums[mid]:
            print(f'{search_num} is in the list')
            found = True
            break
        
        # dịch chuyển high pointer xuống
        # để tìm kiếm sub-array bên tay trái
        if search_num < nums[mid]:
            high = mid - 1

        # dịch chuyển low pointer lên trên mid pointer
        # tìm array bên phải
        elif search_num > nums[mid]:
            low = mid + 1

    if not found:
        print(f'{search_num} is not in the list')
    



# [1, 2, 3, 4, 5] X, [6, 7, 8, 9, 10]
# [6, 7, ] [8, 9, 10]
# 7 

# input: search number: 7
# 7 is in the list

# input: search number: 11
# 7 is not in the list

# Use BINARY SEARCH


# Dictionary: A B C ... X Y Z

# car



# Big O notation:
#     - Linear search: O(n)
#     - Binary search: O(log2(n))

# n = 100
#     - Linear search: max 100 searches
#     - Binary search: max 7 searches


# Selection sort
# O(n^2)

import random
rand_nums = [random.randint(1, 100) for _ in range(10)]

print('Before:', rand_nums)

for i in range(len(rand_nums) - 1):
    smallest_index = i
    for j in range(i + 1, len(rand_nums)):
        if rand_nums[j] < rand_nums[smallest_index]:
            smallest_index = j
        
    # swap 2 numbers
    if smallest_index != i:
        temp = rand_nums[i]
        rand_nums[i] = rand_nums[smallest_index]
        rand_nums[smallest_index] = temp
    
            
print('After:', rand_nums)