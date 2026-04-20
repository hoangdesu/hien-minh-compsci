# sử dụng list: lưu trữ giá trị người dùng nhập vào
# sport_list = []

# for i in range(1, 4):
#     sport = input(f'Enter sport {i}: ')
#     sport_list.append(sport)

# # print(sport_list)

# for sport in sport_list:
#     print(f'I love {sport}')



# Mua 3 món đồ
# Enter name for item 1: macbook pro
# Enter price for item 1: 1000

# Enter name for item 2: iphone 17
# Enter price for item 2: 500

# Enter name for item 3: phone case
# Enter price for item 3: 20

# Show Invoice:
# 1. macbook pro: $1000
# 2. iphone 17: $500
# 3. phone case: $20
# Total: $1520

# Hint: sử dụng 2 list
# 1 list để lưu tên sản phẩm
# 1 list để lưu giá sản phẩm

# item_list = []
# price_list = []

# for i in range(1, 4):
#     item = input(f'Enter name for item {i}: ')
#     price = float(input(f'Enter price for item {i}: '))
#     item_list.append(item)
#     price_list.append(price)
#     print()

# print(f'{item_list=}')
# print(f'{price_list=}')

# i = 0 1 2
# total = 0
# print('--- Invoice ---')
# for i in range(len(item_list)):
#     print(f'{i+1}. {item_list[i]}: ${price_list[i]}')
#     total += price_list[i] # total = total + price

# print(f'Total: ${total}')



# Level 3: add quantity

# Enter name for item 1: macbook pro
# Enter price for item 1: 1000
# Enter quantity for item 1: 3

# Enter name for item 2: iphone 17
# Enter price for item 2: 500
# Enter quantity for item 2: 5

# Enter name for item 3: phone case
# Enter price for item 3: 20
# Enter quantity for item 3: 10

# --- Invoice ---
# 1. macbook pro: $1000 x 3 = $3000
# 2. iphone 17: $500 x 5 = $2500
# 3. phone case: $20 x 10 = $200
# Total: $5700


item_list = []
price_list = []
quantity_list = []

for i in range(1, 4):
    item = input(f'Enter name for item {i}: ')
    price = float(input(f'Enter price for item {i}: '))
    quantity = int(input(f'Enter quantity for item {i}: '))
    item_list.append(item)
    price_list.append(price)
    quantity_list.append(quantity)
    print()

total = 0
print('--- Invoice ---')
for i in range(len(item_list)):
    item_total = price_list[i] * quantity_list[i]
    print(f'{i+1}. {item_list[i]}: ${price_list[i]} x {quantity_list[i]} = ${item_total}')
    total += item_total

print(f'Total: ${total}')