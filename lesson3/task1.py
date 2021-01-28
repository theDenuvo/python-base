def check(c):
    if c == 0:
        print('Error: Division by zero')
        return
    else:
        return c


def division(a, b):
    check(a)
    check(b)
    try:
        print(a/b)
    except ZeroDivisionError:
        return


num1 = int(input())
num2 = int(input())
division(num1, num2)
