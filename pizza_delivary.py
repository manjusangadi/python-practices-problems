#What will be the total bill if a customer orders a Medium pizza with pepperoni and extra cheese?
print('Welcome to python pizza delivary')
size= input('What size pizza do you want? S,M,L:')
add_pepperoni = input('Do you want pepperoni? Y or N:')
add_cheese = input('Do you want cheese? Y or N:')
bill = 0
if size == 'S'or's':
    bill += 20
elif size == 'M'or'm':
    bill += 30
elif size=='L'or 'l' :
    bill += 40
else:
    print('invalid value')

if add_pepperoni == 'Y'or'y':
    bill +=5

if add_cheese == 'Y'or'y':
    bill +=5

print(f'your total bill is :{bill}')

