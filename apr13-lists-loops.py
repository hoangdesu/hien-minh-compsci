# List vs Array

# list: danh sách
# array: chuỗi

# => 1 tập hợp các phần tử có phần liên quan tới nhau
# - các phần tử đều có index (vị trí), bắt đầu từ 0

# food array: gà, chuối, mật ong
# drinks: nc suoi, cam, chanh


# food_list = ['chicken', 'banana', 'honey']

# print(food_list)

# print(f'i love eating {food_list[0]}')
# print(f'i also like {food_list[2]} {food_list[0]}')

# grades = [9.2, 5.2, 7.3]

# total = grades[0] + grades[1] + grades[2]
# print(total)
# average = total / 3
# print(f'{average:.1f}')


# -----
# Iteration (loops) + list
# For loop + while loop

# 0 -> end-1
# for i in range(10):
#     print(i, 'hello')

# start -> end-1
# for x in range(15, 21):
#     print(x)

# start -> end-1, with step+2
# for y in range(1, 20, 2):
#     print(y)

# di nguoc xuong
# for m in range(10, 0, -1):
#     print(m)
    
    
# grades = [9.2, 5.2, 7.3, 7.1, 8.8, 1.0, 3.2, 4.5, 5.9, 7.7, 8.8, 6.6]

# # print('len:', len(grades))

# # Accumulation: gom lại
# total = 0

# for i in range(len(grades)):
#     # print(grades[i])
#     total = total + grades[i]
    
# # print(total)
# average = total / len(grades)
# print('Average score:', average)



# Spendings

# input price for 3 items
# calculate the total for 3 items

# # 1. lấy input
# enter price for item 1: 30
# enter price for item 2: 65
# enter price for item 3: 10

# # 2. tính tổng
# total is 105k

total_price = 0
for i in range(1, 4):
    price = float(input(f'enter price for item {i}: '))
    total_price = total_price + price
    
print(f'Total price: ${total_price}')

