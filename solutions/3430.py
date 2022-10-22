string = input()
for index, char in enumerate(string):
    print((index + 1) * char + string[index + 1:])
