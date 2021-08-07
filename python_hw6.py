#https://projecteuler.net/problem=36

#The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
#Find the sum of all numbers, less than one million, which are palindromic in
#base 10 and base 2. (Please note that the palindromic number,
#in either base, may not include leading zeros.)

#Напишите программу, которая решает описанную выше задачу и печатает ответ.

#Для более компактного вида программы испольхуем list comprehensions

list_10_pol=[i for i in range(1,1000001) if str(i)==str(i)[::-1]]   #Выбираем из диапазона 1-1000000 все числа, являющиеся палиндромами
list_2_1=[bin(i)[2:] for i in list_10_pol]                          #Преобразуем полученный список в двоичное представление
list_2_pol=[i for i in list_2_1 if i == i[::-1]]                    #Выбираем палиндромы из полученного списка
list_2_pol_int=list(map(int,list_2_pol))                            #Преобразуем элементы списка в тип int
list_10_pol_int=[int(str(i), 2) for i in list_2_pol_int]            #Преобразуем список в десятичное представление
print(sum(list_10_pol_int))                                         #Получаем сумму всех чисел-палиндромов от 1 до 1000000





