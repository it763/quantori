#Написать функцию Фиббоначи fib(n), которая вычисляет
#элементы последовательности Фиббоначи:
#1 1 2 3 5 8 13 21 34 55 .......
#Программа возвращает указанный элемент последовательности
n = input('Введите количество элементов последовательности Фиббоначи: ')
def fib(n):
    m=int(n[:])
    n = int(n)
    list1 = []
    if n == 1:
        list1.append(1)
    elif n == 2:
        list1.append(1)
        list1.append(1)
    else:
        list1.append(1)
        list1.append(1)
        f1=f2=1
        while int(n)!=0:
            f1,f2 =f2,f1+f2
            list1.append(f2)
            n=n-1
    print(list1[m-1])

fib(n)





