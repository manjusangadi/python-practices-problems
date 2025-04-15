
print('Welcome to treasure island ')
print('Your mission is find the treasure')

choice = input('your at a cross the road, where do you want to go? Type "Left" or "Right":')
choice_1= choice.lower()

if choice_1 == 'left' :
    print(choice_1)
    choice_2 = input('You`ve come to the ocean.There is an island in the middle of the ocean. Type "wait" for boat will come or type "swim" you can swim:').lower()
    if choice_2  == 'wait':
        print(choice_2)
        choice_3= input('You arrive at the island unharmed. There is an house with 3 doar`s  choose any one red,yellow,green:').lower()
        if choice_3 == 'red':
            print('It is not a room full of fire. Game over')
        elif choice_3 == 'yellow':
            print('You found the treasure. you win')
        else:
            print('It is not a room. Game over')
    else:
        print('Game over')

else:
    print('You fell into the hole. Game over')
