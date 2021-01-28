# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента и возвращает сумму наибольших двух аргументов
def max_sum(a, b, c):
    nums = [a, b, c]
    nums.sort()
    nums[0] = 0
    return sum(nums)


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(max_sum(num1, num2, num3))