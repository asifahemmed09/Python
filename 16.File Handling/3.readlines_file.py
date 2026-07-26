f = open("demo.txt")

lines = f.readlines()

for line in lines:
    print(line.rstrip())


f.close()
