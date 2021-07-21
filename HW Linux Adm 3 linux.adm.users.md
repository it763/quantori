## HW Linux Adm 3 linux.adm.users  
  
В папке /var/ftp/ - есть подпапки пользователей (/var/ftp/ivan, /var/ftp/aleksei, etc.), куда они складывают свои файлы.  
Есть пользователь и группа ftp-admin - они используются администратором ftp сервера, и он может управлять содержимым всех подпапок всех пользователей. При этом обычные пользователи могут управлять только своими файлами.  
  
Написать скрипт для добавления новых пользователей ftp-сервера в систему. Скрипт должен генерировать пароль, добавлять пользователя в систему, настраивать права пользователя, создавать домашний каталог.  
  
Пишем скрипт, который будет принимать в качестве аргурмента имя нового пользователя.
Предварительно нужно установить программу генерации случайных паролей **pwgen**.  



**#! /bin/bash**  
**useradd  -s /bin/bash -m $1**   #заводим пользователя с оболочкой /bin/bash  и создаем ему домашний каталог.  
**password=$(pwgen -1 -s -n 10)**  #С помощью программы pwgen генерируем случайный пароль из 10 символов  
**echo $1:${password} | chpasswd**  #Задаем пользователю сгенерированный пароль  
**mkdir /var/ftp/$1**  #Заводим директорию ftp  
**chown -R $1 /var/ftp/$1**  #Делаем нового пользователя владельцем директории  
**chown -R .ftp-admin /var/ftp/$1** #Назначаем группу владельца ftp-admin  
**chmod -R g+rw /var/ftp/$1** #Назначаем права для группы  
**chmod -R g+s /var/ftp/$1**   #Устанавливаем GUID для папки, чтобы все вновь создаваемые файлы имели группу-владельца ftp-admin.  
**chmod -R o-rwx /var/ftp/$1** #Отбираем права у остальных  
**chmod -R u+rw /var/ftp/${1}** #Назначаем права пользователю  
**echo Created new user $1 with password ${password}**  #Сообщаем имя пользователя и пароль 
  

**Проверка работы скрипта**  
  
[admin@devops ~]# sudo ./useradd.sh alex  
Created new user alex with password 2I77dAdX6C  
  
**Проверяем наличие записи в /etc/passwd**  
  
[admin@devops root]$ cat /etc/passwd | grep alex  
alex:x:1009:1009::/home/alex:/bin/bash  
  
Появился пользователь alex с оболочкой /bin/bash и домашним каталогом /home/alex  
  
**Проверяем наличие записи в /etc/shadow**  
[admin@devops root]$ sudo cat /etc/shadow | grep alex  
  
alex:$6$7Zal8/z9IhB$W.5kPmlHPt6zH03OEPG/Sq3fbXnpO0yVBeWFDvOHt0fX2/Rll7zsDuxWy7y2GKv8wlvs1Lrex3TC262KXvDxL.:18829:0:99999:7:::  
  
**Проверяем наличие папки в /var/ftp и назначение прав**  
  
[admin@devops root]$ ls -l /var/ftp/ | grep alex  
drwxrws---. 2 alex  ftp-admin   6 Jul 21 14:34 alex  


  











  

