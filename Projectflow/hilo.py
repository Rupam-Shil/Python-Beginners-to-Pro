low = 1
high = 1000

print('Please think a number between {} and {}'.format(low, high))
input('Press ENTER to start')

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}.Should I guess higher or lower?(h/l) "
                     "or c if i guess correct"
                     .format(guess)).casefold()
    if high_low == 'h':
        low = guess+1
    elif high_low == 'l':
        high = guess-1
    elif high_low == 'c':
        print("wipee i guess the correct {}".format(guess))
        break
    else:
        print("Please enter l,h or c")
    guesses += 1
else:
    print(guesses)


