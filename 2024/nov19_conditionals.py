# Conditionals

# is_raining = False

# if is_raining == True:
#     print('Stay inside')
# else:
#     print('Go outside')

# boolean: Data types, True/False

# == -> Comparison operator: phep so sanh
# =  -> Assignment operator: phep gan


# neu nhat -> konnichiwa
# neu vn -> xin chao
# tbn -> hola
# tq -> ni hao
# phap -> bonjour
# han -> annyeong
# others -> hello

# country = input('Where are you from: ')

# if country == 'japan':
#     print('Konnichiwa')
# elif country == 'vietnam' or country == 'viet nam' or country == 'Vietnam' or country == 'Viet Nam':
#     print('Xin chao')
# elif country == 'spain':
#     print('Hola')
# elif country == 'france':
#     print('Bonjour')
# elif country == 'china':
#     print('Ni hao')
# else:
#     print('Hello')


saved_username = 'minh'
saved_password = '0bik'

saved_username2 = 'brian'
saved_password2 = 'hehe'

username = input('Enter your username: ')
password = input('Enter your password: ')

if username == saved_username and password == saved_password: 
    print('Login successfully! Welcome ' + username)
elif username == saved_username2 and password == saved_password2:
    print('Login successfully! Welcome ' + username)
else:
    print('Login failed')
