#guess the number

secret_number = 9

guess_count = 1

while guess_count <= 3:
    guess = int(input('guess no: '))
    guess_count += 1

    if guess == secret_number:
        print('you won')
        break
else:
    print('your guess wrong no')


