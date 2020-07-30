data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
# data = [104, 101, 105, 308, 103,
#         107, 100, 306, 106, 102, 108]
# data = [104, 101, 4, 105, 103, 5,
#         107, 100, 106, 102, 108]
# data = [104, 101, 105, 103,
#         107, 100, 106, 102, 108]
# data = []

min_valid = 100
max_valid = 200

# REVERSE A LIST PROCESS 1

for index in range(len(data)-1, -1, -1):
    if data[index] < min_valid or data[index] > max_valid:
        print(index, data)
        del data[index]

# REVERSE A LIST PROCESS 2


top_index = len(data) - 1
for index, values in enumerate(reversed(data)):
    if values < min_valid or values > max_valid:
        print(top_index - index, values)
        del data[top_index - index]

print(data)
