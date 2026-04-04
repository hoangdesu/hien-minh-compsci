

# function: re-useable blocks of code
#     params - parameters
#     return value

# 1. define
def add(a, b):
    c = a + b
    # print(c)
    return c
    

# 2. function execution / run / invoke

print(add(1, 2) * 4)
# print(3 * 4)

total = add(3, 5)
print(total)




def hi(name: str):
    # message = f'Hi my name is {name}'     # string format
    message = 'Hi my name is ' + name       # string concatenation
    print(message)
    
    
# hi('Hien Minh')
# hi('Brian')
# hi('Hoang')


def introduce(name, age, country):
    print(f'Hi my name is {name}, I am {age} and I came from {country}')


# introduce('Hien Minh', 17, 'Vietnam')                   # positional arguments
# introduce(country='Vietnam', name='Brian', age=30)      # named arguments



# name = input('Enter your name: ')
# print('hello ' + name)