with open("test.txt","w") as f:
    lines = ["Hello\n","This is a test file.\n","Is there everything alright"]
    for line in lines:
        f.writelines(line)

