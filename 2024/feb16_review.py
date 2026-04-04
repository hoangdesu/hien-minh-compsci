# ask for name

name = input('Hello what is your name: ') # input always returns a string
print('hello ' + name)

# ask for age
age = int(input(name + ', how old are you: '))
# print(age)

# calculate birthyear from age
birth_year = 2024 - age

# display birthyear
print('So you were born in ' + str(birth_year))

# Phan loai:
# - kids: 1-17
# - adult: 18-50
# - seniors: 50-100

# Conditionals: if-elif-else
if age >= 1 and age <= 17:
    print('You are a kid')
elif age >= 18 and age <= 50:
    print('You are an adult')
elif age >= 50 and age <= 100:
    print('You are a senior')
else:
    print('Invalid age')

# ...

# Data types:
#     - str
#     - int
#     - float
#     - bool
    
    
# Math: + - * / pow

HW: BMI calculator

Cho user input:
    weight kg
    height cm 1.73m -> 173cm

cong thuc tinh BMI -> google

Your BMI is 27. You are overweight, you should exercise more

Your BMI is 17. You are underweight, you should eat more

