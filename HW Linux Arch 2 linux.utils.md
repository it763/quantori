## HW Linux Arch 2 linux.utils
* Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который считает количество файлов в полном имени (включая путь) которых есть подстрока “root”, но нет подстроки “proc”.  
 **find  -type f | grep root | grep -v proc | wc -l**  
 Ищем в текущем каталоги все файлы ==> отбираем те, у которых в названии присутствует root ==> из них отбираем те, у которых отсуствует proc в названии ==> передаем программе wc, считаем сколько таких файлов нашлось.  
   
* Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который выводит значящие (не закомментированные и не пустые) строки файла конфигурации сервиса. Например из файла /etc/ssh/sshd_config  
 **cat /etc/ssh/sshd_config | grep -v ^# | grep -v ^$**  
 Читаем файл /etc/ssh/sshd_config ==> ищем в нем строки, начинающиеся с #, исключаем их их вывода grep ==> ищем просто пустые строки и исключаем их из выводв команды grep.  
   
* Выбрать все уникальные оболочки из файла /etc/passwd и сравнить со списком оболочек из файла /etc/shells  
**cut -d: -f7 /etc/passwd | sort | uniq  > res1.txt**  
**cut -d: -f7 /etc/shells | sort | uniq > res2.txt**  
С помощью программы cut разбиваем файлы /etc/passwd и /etc/shells на поля по разделителю :. (Зная структуру этих файлов). Выводим значения 7 поля (оболочки) ==> Сортируем, выбираем уникальные значения ==> Передаем результаты в файлы.  
**diff res1.txt res2.txt -y**  
Сравниваем файлы командой diff, выводим результат в 2 колонки.  
/bin/bash &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /bin/bash  
/bin/sync &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| /bin/sh  
/sbin/halt &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | /usr/bin/bash  
/sbin/nologin &nbsp; &nbsp; &nbsp; | /usr/bin/sh  
/sbin/shutdown &nbsp; &nbsp;<  





   

