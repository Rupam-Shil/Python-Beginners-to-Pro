empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)
print()

for number_list in numbers:
    print(number_list)

    for values in number_list:
        print(values)














# sorted_numbers = sorted(numbers)
# print(sorted_numbers)
#
# digits = list("423985617")
# print(digits)
#
# # more_numbers = list(numbers)
# # # more_numbers = numbers[:]
# more_numbers = numbers.copy()
# print(more_numbers)
#
#
#
# print(numbers is more_numbers)
#
# # print(id(even))
# # even.extend(odd)
# # print(even)
# #
# # even.sort()
# # print(even)
# # print(id(even))
# #
# # even.sort(reverse=True)
# # print(even)
# # print(id(even))
