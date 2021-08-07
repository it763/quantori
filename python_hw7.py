#Напишите программу, которая читает данные из файлов
#/etc/passwd и /etc/group на вашей системе и выводит
#следующую информацию в файл output.txt:
#1. Количество пользователей, использующих все имеющиеся
#интерпретаторы-оболочки.
#( /bin/bash - 8 ; /bin/false - 11 ; ... )
#2. Для всех групп в системе - UIDы пользователей
#состоящих в этих группах.
#( root:1, sudo:1001,1002,1003, ...)

from collections import Counter
out= open('output.txt','w')                           #Отркыть файл, куда будут выводиться результаты
f=open("passwd")                                      #Открыть файл passwd
user_lines=f.readlines()                              #Создать список, в котором каждый элемент - строка файла passwd
user_lines=[i.rstrip('\n') for i in user_lines]       #Убирается переевод строки у каждого элемента списка
user_lines_lists=[i.split(':') for i in user_lines]   #Создать список в котором каждый элемент - список из элементов каждой строки файла passwd, разделенных :
user_shells=[i[6] for i in user_lines_lists]          #Создать список из значений оболочек файла passwd
shells_count = dict(Counter(user_shells))             #Создать словарь, в котором пара ключ:значение - оболочка:количество пользователей с такой оболочкой
for k,v in shells_count.items():                      #Вывод результатов в файл
    print(k, '-',v,end=' ; ', file=out)

print('\n', file=out)                                 #Добавление разделительной строки в выходной файл

fg=open("group")                                       #Открыть файл groups
gr_lines=fg.readlines()                                #Создать список, в котором каждый элемент - строка файла group
gr_lines=[i.rstrip('\n').rstrip(':') for i in gr_lines]    #Убирается переевод строки и : в конце у каждого элемента списка
gr_lines_lists=[i.split(':x:') for i in gr_lines]      #Создать список в котором каждый элемент - список из элементов каждой строки файла passwd, разделенных :x:
for k1,v1 in dict(gr_lines_lists).items():             #Создать словарь, в котором пара ключ:значение - имя группы:uid пользователя в ней
    print(k1, ':', v1, end=',', file=out)              #Вывод результатов в файл
f.closed                                               #Закрыть используемые файлы
fg.closed
out.closed
