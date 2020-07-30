#
#       01234567890123
parrot="Norwegian Blue"
#SLICING
print((parrot[0:6]))
print(parrot[:9])
print(parrot[10:])
print(parrot[:6]+parrot[6:])
print(parrot[:])
print(parrot[-6:-3])
print(parrot[0:6:2])
number='9,223;372:036 854,775;807'
separators=number[1::4]

values="".join(char if char not in separators else " " for char in number).split()
print(values)
print([int(val) for val in values])




