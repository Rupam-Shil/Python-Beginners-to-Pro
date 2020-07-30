available_parts = ['computer',
                   'monitor',
                   'keyboard',
                   'mouse pad',
                   'hdmi cable',
                   'dvd drive'
                   ]
current_choice = '-'
computer_parts = []
valid_choice = [str(i) for i in range(1, len(available_parts) + 1)]
print(valid_choice)
while current_choice != '0':
    if current_choice in valid_choice:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # its already in
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)

        else:
            print("adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please add options from the list below")
        for numbers, part in enumerate(available_parts):
            print("{}: {}".format(numbers + 1, part))
        print("0: Exit")
    current_choice = input()
print("Your choices contain:-")
for item in computer_parts:
    print(item)
