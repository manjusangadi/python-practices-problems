
price = float(input('Enter the price of product :'))
google_pay = True
if google_pay:
    discount = 0.2 * price
else:
    discount = 0.1 * price

print(f'Discount price : {discount}')
