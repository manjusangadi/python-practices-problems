# comparison operartor
#Write a Python program that:
# Asks the user to enter their name.
# Checks the length of the name:
# If the name has less than 3 characters, display:
# "your name is simple "
# If the name has more than 14 characters, display:
# "your name is long"
# Otherwise, display:
# "your name is valid"

user_name = input('Enter your name: ')

if len(user_name) <= 3:
    print('your name is simple ')
elif len(user_name)>14:
    print('your name is long')
else:
    print('your name is valid ')



