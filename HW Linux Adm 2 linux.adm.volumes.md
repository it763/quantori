## HW Linux Adm 2 linux.adm.volumes  
  
**Рассчитать вероятность потерять данные при использовании дисков в raid массиве, для разных raid level и разных количествах дисков. Считать вероятность выхода из строя одного диска - 1%.
Рассчитать насколько уменьшится суммарный объем памяти при использовании дисков в raid массиве, для разных raid level и разном количестве дисков, по сравнению с использованием дисков как независимых.**
  
Расчет приизведен по формуле Pr(X) = (n"COMBINATION"X) * (p)^X * (1-p)^(n-X)  
n- количество дисков в массиве  
X -количество дисков, которые должны выйти из строя чтоб массив полностью вышел из строя  
p - вероятность выхода из строя одного диска  
n"COMBINATION"X - биномиальный коэффициент  
  
Расчеты вероятности выхода из строя массива и изменения суммарного объема дискового пространства:  
raid0 2 диска Вероятность выхода из строя - 1.98%; Объем не меняется     
raid0 4 диска Вероятность выхода из строя - 3.88%; Объем не меняется  
  
raid 1 2 диска Вероятность выхода из строя - 0.01%; Объем уменьшится на 50%  
raid 1 4 диска Вероятность выхода из строя - 0.058%; Объем уменьшится на 50%  
  
raid 5 3 диска Вероятность выхода из строя - 0.0297%; Объем уменьшится на 30%  
raid 5 5 дисков Вероятность выхода из строя - 0.097%; Объем уменьшится на 20%  
  
raid 6 5 дисков Вероятность выхода из строя - 0.0009%; Объем уменьшится на 40%  
raid 6 7 дисков Вероятность выхода из строя - 0.0033%; Объем уменьшится на 28.5%  
  
  
**Собрать несколько lv поверх md (raid5). Смонтировать с разными опциями в дерево каталогов.**   
Добавляем в систему 3 диска, из которых будет собран массив raid5 (sdb, sdc, sdd)  
**[root@co1 admin]# sfdisk -s**  
/dev/sdd:   1048576  
/dev/sda:  20971520  
/dev/sdc:   1048576  
/dev/sdb:   1048576  
  
На всякий случай зануляем суперблоки на дисках, они могут содержать информацию о других массивах, если диски ранее использовались.  
**mdadm --zero-superblock --force /dev/sd{b,c,d}**  
Получаем  
[root@co1 admin]# mdadm --zero-superblock --force /dev/sd{b,c,d}  
mdadm: Unrecognised md component device - /dev/sdb  
mdadm: Unrecognised md component device - /dev/sdc  
mdadm: Unrecognised md component device - /dev/sdd  
Диски ренее не использоватлись в raid, можно продолжать настройку. 
  
Собираем raid5  
**mdadm --create --verbose /dev/md0 -l 5  -l 3 /dev/sd{b,c,d}**  
/dev/md0 - устройство, котрое появится после сборки массива  
-l 5 - указываем уровень raid 5  
-n 3 - указываем количество дисков в массиве  
-/dev/sd{b,c,d} указываем диски, из которых будет собран массив  
Проверим статус массива  
cat /proc/mdstat  
 
[root@co1 admin]# cat /proc/mdstat  
Personalities : [raid6] [raid5] [raid4]  
md0 : active raid5 sdd[3] sdc[1] sdb[0]  
      2093056 blocks super 1.2 level 5, 512k chunk, algorithm 2 [3/3] [UUU]  
        
  
Создаем файл mdadm.conf для внесения инфомации о массиве  
**mkdir /etc/mdadm  
touch /etc/mdadm/mdadm.conf**  
  
  
**[root@co1 admin]# cat /etc/mdadm/mdadm.conf  
DEVICE partitions  
ARRAY /dev/md0 level=raid5 num-devices=3 metadata=1.2 name=co1:0 UUID=eedce199:51500c9d:1c7be6f5:b5c12d3a**  
  
Просмотр подробной информации о массиве  
**mdadm -D /dev/md0**  

[root@co1 admin]# mdadm -D /dev/md0  
/dev/md0:  
           Version : 1.2  
     Creation Time : Sun Jul 18 18:13:11 2021  
        Raid Level : raid5  
        Array Size : 2093056 (2044.00 MiB 2143.29 MB)  
     Used Dev Size : 1046528 (1022.00 MiB 1071.64 MB)  
      Raid Devices : 3  
     Total Devices : 3  
       Persistence : Superblock is persistent  
  
       Update Time : Sun Jul 18 18:13:23 2021  
             State : clean  
    Active Devices : 3  
   Working Devices : 3  
    Failed Devices : 0  
     Spare Devices : 0  
  
            Layout : left-symmetric  
        Chunk Size : 512K  
  
Consistency Policy : resync  
  
              Name : co1:0  (local to host co1)  
              UUID : eedce199:51500c9d:1c7be6f5:b5c12d3a  
            Events : 18  
  
    Number   Major   Minor   RaidDevice State  
       0       8       16        0      active sync   /dev/sdb  
       1       8       32        1      active sync   /dev/sdc  
       3       8       48        2      active sync   /dev/sdd  
       
    
  
Переходим к созданию LV.  
Структура LVM состоит из 3 слоев:  
Физический том PV  
Группа физических томов VG  
Логический том LV  

Инициализируем физический том  
**pvcreate /dev/md0**  
[root@co1 admin]# pvcreate /dev/md0  
  Physical volume "/dev/md0" successfully created.  
 
Посмотреть PV  
 **pvscan**  
 [root@co1 admin]# pvscan  
  PV /dev/sda2   VG centos          lvm2 [<19,00 GiB / 0    free]  
  PV /dev/md0                       lvm2 [<2,00 GiB]  
  Total: 2 [20,99 GiB] / in use: 1 [<19,00 GiB] / in no VG: 1 [<2,00 GiB]   
    
Создаем группу томов  
**vgcreate vol_gr1 /dev/md0**  
  
[root@co1 admin]# vgcreate vol_gr1 /dev/md0  
  Volume group "vol_gr1" successfully created   
    
[root@co1 admin]# pvdisplay  
  --- Physical volume ---  
  PV Name               /dev/md0  
  VG Name               vol_gr1  
  PV Size               <2,00 GiB / not usable 4,00 MiB  
  Allocatable           yes  
  PE Size               4,00 MiB  
  Total PE              510  
  Free PE               510  
  Allocated PE          0  
  PV UUID               iUMHhm-j1GR-6WCM-dwBe-Exye-JIcA-uCJXci  
    
 
Создаем логические тома  
**lvcreate -L 100M -n Logical_volume1 vol_gr1   
lvcreate -L 100M -n Logical_volume2 vol_gr1   
lvcreate -L 100M -n Logical_volume3 vol_gr1**   
  
3 тома размером по 100 МБ.  
  
Отформатируем тома в ext4  
**mkfs.ext4 /dev/vol_gr1/Logical_volume1  
mkfs.ext4 /dev/vol_gr1/Logical_volume2  
mkfs.ext4 /dev/vol_gr1/Logical_volume3**  
  
Примонтируем тома с разными опциями. (lv1 - только для чтения, lv2 - обычный режим r/w, lv3 - с опцией noexec, запретом на запуск исполняемых файлов)  
**mkdir /mnt/lv1 && mount -r /dev/vol_gr1/Logical_volume1 /mnt/lv1  
mkdir /mnt/lv2 && mount  /dev/vol_gr1/Logical_volume2 /mnt/lv2  
mkdir /mnt/lv3 && mount -o noexec /dev/vol_gr1/Logical_volume3 /mnt/lv3**  
  
Проверяем монтирование томов  
[root@co1 admin]# mount | grep Logic  
/dev/mapper/vol_gr1-Logical_volume1 on /mnt/lv1 type ext4 (ro,relatime,seclabel,stripe=1024,data=ordered)  
/dev/mapper/vol_gr1-Logical_volume3 on /mnt/lv3 type ext4 (rw,noexec,relatime,seclabel,stripe=1024,data=ordered)  
/dev/mapper/vol_gr1-Logical_volume2 on /mnt/lv2 type ext4 (rw,relatime,seclabel,stripe=1024,data=ordered)  
  

Для того чтобы тома монтировались при старте системы редактируем **/etc/fstab**, вносим строки  
**/dev/mapper/vol_gr1-Logical_volume1 /mnt/lv1  ext4 ro,relatime,seclabel,stripe=1024,data=ordered 0 0  
/dev/mapper/vol_gr1-Logical_volume2 /mnt/lv2 ext4 rw,relatime,seclabel,stripe=1024,data=ordered 0 0  
/dev/mapper/vol_gr1-Logical_volume3 /mnt/lv3 ext4 rw,noexec,relatime,seclabel,stripe=1024,data=ordered 0 0**  
 





