def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('/ = exit').split()

        res = 0
        for el in range(len(number)):
            if number[el] == '/'
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(sum_res)
    print(f'final sum: {sum_res}')


my_sum() 
