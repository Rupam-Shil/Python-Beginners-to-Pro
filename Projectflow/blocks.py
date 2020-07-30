name= input("Please Enter Your Name: ")
age = int(input("How old are you,{0}?".format(name)))
print(age)

if age<=18 :
    print("Please come back after {0} years".format(18 - age))

elif age==100:
    print("Maybe you should have died")
else:
    print("Your are eligible")
