def ascii_convertor(a):
    num_ascii = ord(a)
    num_ascii -= 32
    a = chr(num_ascii)
    return a


string = list(input())
for i in range(len(string)):
    if i == 0 or ord(string[i - 1]) == 32:
        string[i] = ascii_convertor(string[i])
for elem in string:
    print(elem, end='')
