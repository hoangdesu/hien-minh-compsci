# cho phep user nhap so lien tuc
# den khi user nhap so 0, thi dung lai

# Enter a number: 8
# Enter a number: 9
# Enter a number: 1
# Enter a number: 0
# 8 + 9 + 1 = 18
# Total = 18

# bai 1:
# total = 0

# while (True):
#     num = int(input('Enter a number: '))
    
#     if num == 0:
#         break
#     else:
#         total += num
        
# print('Total: ' + str(total))



# iteration vs looping la 1
# 2 kieu: for loop vs while loop
# - for loop: loop within a range
# - while loop: loop when condition is met

# totaling va counting: 2 ky thuat lap trinh
# ko lien quan den vong lap


# bai 2:

# total = 0
# numbers = [] # khoi tao 1 list rong

# while (True):
#     num = int(input('Enter a number: '))
    
#     if num == 0:
#         break
#     else:
#         total += num
#         numbers.append(num)
        
# for i in range(len(numbers)):
#     print(numbers[i], end="")
#     if i == len(numbers) - 1:
#         print(" = ", end="")
#     else:
#         print(' + ', end="")
    
# print(total)



# Exercise: create a game library app
    
    
# Welcome to Minh's game library

# Enter your favorite game: lien minh
# Added lien minh to your game library

# Enter your favorite game: toc chien
# Added toc chien to your game library

# Enter your favorite game: pubg
# Added pubg to your game library

# Enter your favorite game: roblox
# Added roblox to your game library

# Enter your favorite game: exit()

# You have 4 games in your library:
# 1. lien minh
# 2. toc chien
# 3. pubg
# 4. roblox

# Thank you. Bye bye!

# 1. input/output + variable
# 2. branchings: if/elif/else
# 3. for/while loops
# 4. list

print("Welcome to Minh's game library")

game_library = []

# Step 1: input
while(True):
    game = input('Enter your favorite game: ')
    
    if game == 'exit()':
        break
    else:
        game_library.append(game)
        print('Added ' + game + ' to your library!\n')
       
# Step 2: output
print('You have ' + str(len(game_library)) + ' games in your library:')
for i in range(len(game_library)):
    print(str(i+1) + '. ' + game_library[i])