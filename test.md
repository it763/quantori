## HW Linux Arch 2 linux.utils
* Используя bash и программы из пакетов util-linux и core-utils, составить pipeline, который считает количество файлов в полном имени (включая путь) которых есть подстрока “root”, но нет подстроки “proc”.
 find  -type f | grep root | grep -v proc | wc -l
 Ищем в текущем каталоги все файлы ==> отбираем те, у которых в названии присутствует root ==> из них отбираем те, у которых отсуствует proc в названии ==> передаем программе wc, считаем сколько таких файлов нашлось.