## HW Linux Arch 2 linux.utils
* Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который считает количество файлов в полном имени (включая путь) которых есть подстрока “root”, но нет подстроки “proc”.  
 **find /  -type f -name '\*root\*' -not -name '\*proc\*' | wc -l**  
 Ищем в корневом каталоги все файлы в имени которых присутствует root и отсутствует proc ==> передаем программе wc, считаем сколько таких файлов нашлось. Поиск в корне нужно запускать с привелегиями суперпользователя. Иначе получим отказ при доступе к части папок.  
   
 
   
* Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который выводит значящие (не закомментированные и не пустые) строки файла конфигурации сервиса. Например из файла /etc/ssh/sshd_config  
 **cat /etc/ssh/sshd_config | grep -v ^# | grep -v ^$**  
 Читаем файл /etc/ssh/sshd_config ==> ищем в нем строки, начинающиеся с #, исключаем их из вывода ==> ищем просто пустые строки и исключаем их из вывода.  
   
* Выбрать все уникальные оболочки из файла /etc/passwd и сравнить со списком оболочек из файла /etc/shells  
**cut -d: -f7 /etc/passwd | sort | uniq  > res1.txt**  
С помощью программы cut разбиваем файл /etc/passwd на поля по разделителю :. (Зная структуру файла). Выводим значения 7 поля (оболочки) ==> Сортируем, выбираем уникальные значения ==> Передаем результаты в файл.  


  Сравниваем файлы командой diff, выводим результат в 2 колонки.  
  **diff res1.txt /etc/shells -y**   
  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  > /bin/sh  
  /bin/bash &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp;                                                         /bin/bash  
  /bin/sync &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp;                                                       | /usr/bin/sh  
  /sbin/halt &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp;                                                      | /usr/bin/bash  
  /sbin/nologin &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp; &nbsp;                                                <  
  /sbin/shutdown &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp;   &nbsp; &nbsp;                                                 <  









   

