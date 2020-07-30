pangram = """The quick brown fox
 jumps \t over
  the lazy dog"""

words = pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
values_list = numbers.split(',')
print(values_list)

for index,item in enumerate(values_list):
    values_list[index] = int(item)
print(values_list)

#create a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))

print(integer_values)


