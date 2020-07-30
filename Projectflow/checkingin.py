parrot = "Norweigian Blue"

letter = input("Enter the letter you wanna find: ")

if letter in parrot:
    print("{} is found in {}".format(letter,parrot))
else:
    print("Not found")