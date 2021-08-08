#Встроенная функция input позволяет ожидать и возвращать данные из стандартного
#ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
#Используя данную функцию, напишите программу, которая:

#1. После запуска предлагает пользователю ввести текст.
#2. Проверяет и, если возможно, преобразовывает полученный текст в число,
#используя рекурсивную функцию.
#Если число четное - делит его на 2 и выводит результат.
#Если число нечетное - умножает на 3 и прибавляет 1.
#После чего ждет следующего ввода.
#3.При получении в качестве вводных данных 'cancel' завершает свою работу.

#Определяем функции проверки четности, которые будут рекурсивно выхывать друг друга.
def is_even(n):
    if n ==0:
        return True
    else:
        return is_odd(n-1)

def is_odd(n):
    if n ==0:
        return False
    else:
        return is_even(n-1)


while True:
    in_str=input('Введите текст: ')
    if in_str == 'cancel':
        print ('Bye!')
        break
    elif in_str.isdigit():                                            #Првоеряем являются ли введенные данные числом
        in_number=int(in_str)
        if is_even(in_number):                                        #Проверка на четность
            res=int(in_number/2)
            print (res)
        else:
            res = int((in_number*3)+1)
            print(res)
    else:
        print('Не удалось преобразовать введенный текст в число')






