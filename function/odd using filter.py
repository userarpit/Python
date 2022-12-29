mylist = [1,3,65,2,4,6]

odd = filter(lambda a : a % 2 != 0, mylist)

for i in odd:
    print(i)