## HW Linux Arch 5 linux.scripting
Программа ping в операционной системе solaris не выводит подробности взаимодействия по icmp, а кратко сообщает о том, доступен ли удаленный сетевой узел:
$ ping google.com
google.com is alive
$ ping eeeerrr.fff.rrr
eeeerrr.fff.rrr is not alive  
* Написать bash скрипт ping.sh - который будет эмулировать поведение программы ping из ОС Solaris.

Будем опираться на вывод команды ping. Мы знаем, что в конце вывода есть строка со статистикой по отправленным и полученным обратно пакетам:  
**1 packets transmitted, 1 received, 0% packet loss, time 0ms**  
В нашем случае будем считать, что если количество принятых обратно пакетов равно 0 - хост не отвечает. Если хотя бы один вернулся, хост активен.  
Скрипт будем запускать с аргументом, в котором нужно указать имя/адрес хоста, доступность которого проверяем.
Результат вывода команды ping заносим во временный файл ~/ping.txt в домашнем каталоге пользователя(чтобы не было проблем с правами на создание файла).  
**ping -c3 $1 > ~/ping.txt**  
Отправляем 3 пакета.  
Из временного файла получаем количество полученных пакетов, присваиваем его переменной count.  
**count=\`cat ~/ping.txt | grep -e "packets transmitted" | cut -d ' '  -f4\`**  
Пишем блок кода, который в случае, если количество полученных пакетов равно 0 (не вернулось ни одного) выводит в stdout строку host is not alive, иначе  - строку host is alive.  
**if [[ ${count} -eq 0 ]]; then echo "$1 is not alive"  ; else echo "$1 is alive" ; fi**  
Удаляем временный файл  
**rm ~/ping.txt**  
  
 В итоге скрипт имеет вид:  
**#! /bin/bash  
ping -c3 $1 > ~/ping.txt  
count=\`cat ~/ping.txt | grep -e "packets transmitted" | cut -d ' '  -f4\`  
if [[ ${count} -eq 0 ]]; then echo "$1 is not alive"  ; else echo "$1 is alive" ; fi  
rm ~/ping.txt**    

Пример выполнения скипта:  
Хост доступен:  
**[admin@devops ~]$ ./ping.sh server  
server is alive**  
  
Хост недоступен (доступ с тестовой машины на mail.ru закрыт):  
**[admin@devops ~]$ ./ping.sh mail.ru  
mail.ru is not alive**  














