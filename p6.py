

height = float(input('Enter height in cm :'))
bill = 0

if height > 120:
    age = int(input('Enter age'))
    if age <12:
        bill=5
        print('pay 5')
    elif age <18:
        bill = 8
        print('Pay 8')
    else:
        bill = 12
        print('pay 12')
    take_snapshot = input('would u take snapshoot pay extrea 3$ enter Y or N:')
    if take_snapshot == 'y' or 'Y':
        bill = bill+3
    print(f'your bill {bill}')
    # else:
    #     print(f'your bill {bill}')
else:
    print('can`t raid')