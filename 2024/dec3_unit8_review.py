# Type Casting

# a = "3"
# b = "5"

# print(int(a) + int(b))

# string concatenation: ghep chuoi

# birth_year = int(input("Enter a your birthyear: "))
# this_year = 2023

# age = this_year - birth_year

# print("Your birthyear is: " + str(birth_year))
# print("and you are " + str(age) + " years old")

# name = 'Minh'
# age = 16
# hobby = 'basketball'

# print('Hi my name is ' + name + ', i am ' + str(age) + 'years old')

# String format
# print(f'Hi my name is {name}, I am {age} years old and I like {hobby}')

# for i in range(100):
#     print(str(i) + '. em se ko tai pham')

hint = 'a country in asia, where anime is created' # japan
print(hint)
country = input('guess the country: ')

while country != 'japan':
    print(hint)
    country = input('wrong. guess again: ')

print('congratulations! the answer is japan')