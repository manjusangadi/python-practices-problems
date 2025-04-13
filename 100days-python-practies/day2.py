# def welcome(first_name,last_name):
#     print(f'Hello your first name is {first_name} and last name is {last_name}')
#     print(f'')
#
# def send(welcom):
#     welcome(first_name="Naresh", last_name="raja")
#     print('manu')
#
# send('d')
#
# number = (input('Enter two digit number:'))
# total = int(number[0]) + int(number[1])
# print('total:',total)

# age = int(input('Enter your age:'))
#
# remaing_year = 90 - age
# remaing_month = remaing_year * 12
# remaing_days = remaing_year * 365
# remaing_week = remaing_year * 52
#
# print(f'You have {remaing_days} days,{remaing_week} weeks and {remaing_month} months complte')

bill = float(input('What was the total bill?\n'))
tip = int(input('what per tip would you liketo give? 12,15 or 10?\n'))
split_bill = int(input('How many pepole spilt this bill?\n'))
tip_amount = tip/100
total_tip_amount = bill * tip_amount
total_bill_amount = bill + total_tip_amount
split_bill_amount = total_bill_amount/split_bill

print(f'Each person should pay:{round(split_bill_amount)}')



