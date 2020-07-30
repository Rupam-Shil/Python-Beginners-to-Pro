# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))
result += 'ish'
print(id(result))
print(id(another_result))
another_result = result
print(id(another_result))