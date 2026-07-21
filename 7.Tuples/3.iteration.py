gender = ("Male","Female","Other")

for i in range(0,len(gender)):
    print(gender[i],end=" ")

print()

for i in gender:
    print(i,end=" ")

print()

for index,value in enumerate(gender):
    print(index,value,sep="-")
