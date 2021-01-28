def check(c):
    if c == 0:
        print('error')
    else:
        return c


def division(a, b):
    check(a)
    check(b)
    print(a/b)


num1 = int(input())
num2 = int(input())
division(num1, num2)
