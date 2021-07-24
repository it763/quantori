## HW Linux Adm 4 linux.adm.init.md
  
Написать systemV init script и systemd service unit для filesharing service. В качестве транспорта для передачи файлов использовать протокол http. Номер tcp порта и папку для раздачи файлов можно вынести в файл с параметрами, можно оставить в скрипте, на ваше усмотрение (предлагаю 8080 и /opt/share). В качестве web сервера предлагаю использовать python -m http.server (или python -m SimpleHTTPServer для python2).
Продемонстрировать работоспособность: start, stop, restart, status.  
  
Для запуска http file server исполльзуется скрипт server.py  
https://github.com/python/cpython/blob/3.9/Lib/http/server.py  

  
**SystemV init script**  
  
#!/bin/bash  
case $1 in  
start)  
#Запускаем http file server  
python3 /opt/server.py 8080 --directory /opt/share 1>/var/log/filesharing_v.log 2>/var/log/filesharing_v.log  &  
#Получаем PID запущенного процесса, записываем его в файл /var/run/filesharing_v.pid  
echo $(ps -u | grep -e " python3 /opt/server.py 8080 --directory /opt/share" | grep -v grep | cut -d " " -f7)>/var/run/filesharing_v.pid  
;;  
stop)  
#Отправляем сигнал sigterm  
kill 15 $(cat /var/run/filesharing_v.pid)  
sleep 5  
#Если процесс на завершился после отправки sigterm, завершаем его с помощью sigkill  
kill 9  $(cat /var/run/filesharing_v.pid) 1>/dev/null 2>/dev/null  
#Удаляем файл с PID процесса  
rm /var/run/filesharing_v.pid  
;;  
restart)  
$0 stop  
$0 start  
;;  
status)  
#Проверяем запущен ли процесс  
if [[ "/opt/server.py" = $(ps -u | grep -e "python3 /opt/server.py 8080 --directory /opt/share" | grep -v grep | cut -d " " -f 27) ]]; then  
echo filesharing_v is running, pid=$(cat /var/run/filesharing_v.pid)  
else  
echo filesharing_v is NOT running  
exit 1  
fi  
;;  
*)  
echo No such command. Use start/stop/restart/status  
esac  
exit 0   
  
Скрипт помещается в  /etc/init.d. Файл назван filesharing_v
  
  
**Демонстрация работы сервиса**  
[root@devops init.d]# service filesharing_v start  
[root@devops init.d]# service filesharing_v status  
filesharing_v is running, pid=131229  
[root@devops init.d]# service filesharing_v restart  
[root@devops init.d]# service filesharing_v status  
filesharing_v is running, pid=131793  
[root@devops init.d]# service filesharing_v stop  
[root@devops init.d]# service filesharing_v status  
filesharing_v is NOT running  
  
**Systemd service unit**  
  
Для добавления сервиса в systemd пишем unit. Это конфигурационный файл сервиса. Размещаем в /etc/systemd/system. Файл (соответственно сервис) назван filesharing.service.  
  
[Unit]  
Description=FilesharingService #Описание сервиса  
After=network.target  #Указываем чтобы сервис запускался после запуска сетевой службы
  
[Service]  
Type=simple  
ExecStart=python3 /opt/server.py 8080 --directory /opt/share   
Restart=always  
  
[Install]  
WantedBy=multi-user.target  
  
После добавления юнита нужно перезагрузить конфигурацию сервисов systemd.  
systemctl daemon-reload  


  
**Демонстрация работы сервиса**  
  
[root@devops system]# systemctl start filesharing.service  
[root@devops system]# systemctl status filesharing.service  
● filesharing.service - FilesharingService  
   Loaded: loaded (/etc/systemd/system/filesharing.service; disabled; vendor preset: disabled)  
   Active: active (running) since Sat 2021-07-24 20:20:47 +04; 3s ago  
 Main PID: 131716 (python3)  
    Tasks: 1 (limit: 35464)  
   Memory: 9.1M  
   CGroup: /system.slice/filesharing.service  
           └─131716 /usr/bin/python3 /opt/server.py 8080 --directory /opt/share  
  
Jul 24 20:20:47 devops.localdomain systemd[1]: Started FilesharingService.  
[root@devops system]# systemctl restart filesharing.service  
[root@devops system]# systemctl status filesharing.service  
● filesharing.service - FilesharingService  
   Loaded: loaded (/etc/systemd/system/filesharing.service; disabled; vendor preset: disabled)  
   Active: active (running) since Sat 2021-07-24 20:20:59 +04; 1s ago  
 Main PID: 131722 (python3)  
    Tasks: 1 (limit: 35464)  
   Memory: 9.1M  
   CGroup: /system.slice/filesharing.service  
           └─131722 /usr/bin/python3 /opt/server.py 8080 --directory /opt/share  
  
Jul 24 20:20:59 devops.localdomain systemd[1]: filesharing.service: Succeeded.  
Jul 24 20:20:59 devops.localdomain systemd[1]: Stopped FilesharingService.  
Jul 24 20:20:59 devops.localdomain systemd[1]: Started FilesharingService.  
[root@devops system]# systemctl stop filesharing.service  
[root@devops system]# systemctl status filesharing.service  
● filesharing.service - FilesharingService  
   Loaded: loaded (/etc/systemd/system/filesharing.service; disabled; vendor preset: disabled)  
   Active: inactive (dead)  
  
Jul 24 20:20:42 devops.localdomain systemd[1]: filesharing.service: Succeeded.  
Jul 24 20:20:42 devops.localdomain systemd[1]: Stopped FilesharingService.  
Jul 24 20:20:47 devops.localdomain systemd[1]: Started FilesharingService.  
Jul 24 20:20:59 devops.localdomain systemd[1]: Stopping FilesharingService...  
Jul 24 20:20:59 devops.localdomain systemd[1]: filesharing.service: Succeeded.  
Jul 24 20:20:59 devops.localdomain systemd[1]: Stopped FilesharingService.  
Jul 24 20:20:59 devops.localdomain systemd[1]: Started FilesharingService.  
Jul 24 20:21:08 devops.localdomain systemd[1]: Stopping FilesharingService...  
Jul 24 20:21:08 devops.localdomain systemd[1]: filesharing.service: Succeeded.  
Jul 24 20:21:08 devops.localdomain systemd[1]: Stopped FilesharingService.  

  

  
  

  
 
