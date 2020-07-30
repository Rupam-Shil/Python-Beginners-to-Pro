import random
highest=10
answer=random.randint(1,highest)
print(answer) # TODO: Remove after testing
print('You will get only 5 chances')
i=5
print("Please guess the number from 1-{0}:\n".format(highest))
guess = 0
while guess != answer:
    guess = int(input())
    if i ==1:
        print('you lost all your chances')
        break

    else:
        i=i-1
        print(f'{i} chances are left')

        if guess == answer:
            print("hurrah you guessed correct")
            break
        else:
            if guess ==0:
                break
            elif guess > answer:
                print('Please guess lower: ')
            else:
                print('Please guess higher: ')
                








