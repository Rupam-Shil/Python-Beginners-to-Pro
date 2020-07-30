lists = ['Learn Pyhton','Learn Java','Go Swiming','Have dinner',
         'Go to bed','exist']
print('Please Choose your option from the list below')
i=1
for item in lists:
    print(str(i)+'. {}'.format(item))
    i += 1
select=int(input())
print('you selected {}'.format(lists[select - 1]))


