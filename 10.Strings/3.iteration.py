text = "Programming"
n = len(text)

for i in range(0,n):
    print(text[i],end=" ")

print()

for char in text:
    print(char,end=" ")

print()

count = 0

while count < n:
    print(text[count],end=" ")
    count += 1

print()

for index,char in enumerate(text):
    print(index,char,sep="-",end=" ")
