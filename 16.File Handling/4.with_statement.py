with open("demo.txt") as f:
    content = f.read(10)
    print(content)

with open("demo.txt") as f:
    for line in f:
        print(line.rstrip())

