if __name__ == '__main__':
    string = input()
    if string.count('0') == len(string):
        print('0')
    else:
        while string.startswith('0'):
            string = string[1:]
        print(string)
