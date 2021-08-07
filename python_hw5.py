#Встроенная функция input позволяет ожидать и возвращать данные из стандартного
#ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
#Используя данную функцию, напишите программу, которая:

#1. После запуска предлагает пользователю ввести неотрицательные целые числа,
#разделенные через пробел и ожидает ввода от пользователя.
#2. Находит наименьшее положительное число, не входящее в данный пользователем
#список чисел и печатает его.


#Например:

#-> 2 1 8 4 2 3 5 7 10 18 82 2
#6

in_str=input('Введите неотрицательные целые числа, разделенные пробелом: ')
in_list_sorted=sorted(list(in_str.split()))    #Преобразуем введеные данные в список, сразу сортируем его
in_list_int=list(map(int,in_list_sorted))      #Преобразуем элементы сортированного списка в int
excluded_list=[]                               #Заводим список, в котором будут числа, не входящие во введенные пользователем числа
for i in range (1,int(max(in_list_sorted))+2):   #Заполняем этот список. +2 - на случай, если все введенные числа идут по порядку.
    if i not in in_list_int:
        excluded_list.append(i)
print(min(excluded_list))                      #Печатаем минимальное число, которое не входит в список введенных пользователем










