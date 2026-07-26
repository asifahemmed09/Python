f = open("demo.txt")

line1 = f.readline()
print(line1.rstrip())
line2 = f.readline()
print(line2.rstrip())
line3 = f.readline()
print(line3.rstrip())

f.close()
