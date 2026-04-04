# cho phep user login 3 lan.
#     - neu dung: login successful
#     - neu sai: cho phep thu lai 3 lan. Neu qua 3 lan se lock account

# save_username = 'brian'
# save_password = 'hi$'

# attempts = 3

# for i in range(3):
#     input_username = input('Enter your username: ')
#     input_password = input('Enter your password: ')

#     if input_username == save_username and input_password == save_password:
#         print('Login successful')
#         break
#     else:
#         attempts = attempts - 1
#         if attempts == 0:
#             print('Login failed. Your account has ben locked')
#         else:
#             print('Login failed. You have ' + str(attempts) + ' more tries.')



# List exercise

# print(food[2])

# input: what do you want to order

# neu mon user order co trong menu: -> your pho is coming in 5 minutes
# neu ko co mon user order -> sorry we dont have pizza

# hint:
# - list
# - if-else + for loop

# index starts from 0

# Linear search: thuat toan tim kiem thang hang

# print(menu[1])

menu = ['pho', 'com', 'hu tiu']

order = input('What do you want to order: ')

found = False

for i in range(len(menu)):
    if order == menu[i]:
        found = True
        break

if found:
    print('Your ' + order + ' is coming in 5 minutes')
else:
    print('Sorry we dont have ' + order)



