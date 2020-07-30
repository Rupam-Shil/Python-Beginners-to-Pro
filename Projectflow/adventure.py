available_exits=['north','east','south','west']

chosen_exis=''
while chosen_exis.casefold() not in available_exits:
    chosen_exis=input("Please enter a direction")
    if chosen_exis.casefold() == 'quit':
        print('Game over')
        break
else:
    print("i am glad u are out")


