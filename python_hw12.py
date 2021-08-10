n = int(input('Введите номер элемента последовательности Фиббоначи: '))

def fib(n):
    f1 = f2 = 1
    for i in range(n - 2):
        f1, f2 = f2, f1 + f2
    return f2
print(fib(n))
