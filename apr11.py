# Conditionals
# - branching

# age = int(input('Enter your age: '))

# if age > 65 and age < 150:
#     print('Senior')
# elif 21 <= age <= 65:
#     print('Adult')
# elif 15 <= age < 21:
#     print('Teenager')
# elif 1 <= age < 15:
#     print('Child')
# else:
#     print('Invalid age')



# BMI calculator

# weight / (height ^ 2)
# kg / m^2

# 1. calculate the BMI number
# 2. tell the user what that number means (underweight, healthy, overweight, obesity)
# 3. suggest system: you need to gain/lose x kg to be healthy


# healthy bmi: 18.5-25 (24) => healthy weight
# now: 85kg
# healthy: 74kg
# lose: 11kg

# You need to lose 11kg to be healthy. Eat less and exercise more
# You need to gain 11kg to be healthy. Eat more and exercise more
# You are in the healthy range. Keep it up!


# Guess the number game

import random

rand_num = random.randint(1, 100)
# print(rand_num)

guess = int(input('Guess: '))

count = 0

while guess != rand_num:
    if guess > rand_num:
        guess = int(input('Guess lower: '))
    elif guess < rand_num:
        guess = int(input('Guess higher: '))
    count += 1
    
print(f'Correct! You got it right in {count} times')



