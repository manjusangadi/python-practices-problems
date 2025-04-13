
bill = float(input('What was the total bill?\n'))
tip = int(input('what per tip would you liketo give? 12,15 or 10?\n'))
split_bill = int(input('How many pepole spilt this bill?\n'))
tip_amount = tip/100
total_tip_amount = bill * tip_amount
total_bill_amount = bill + total_tip_amount
split_bill_amount = total_bill_amount/split_bill

print(f'Each person should pay:{round(split_bill_amount)}')



