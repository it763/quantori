## HW Linux Adm 1 linux.adm.software  

Скачайте свежую версию исходников git. Скомпилируйте и инсталлируйте в каталог /usr/local. Убедитесь, что свежая версия установлена и готова к использованию.  
  
Перед компилированием и установкой установим зависимости git.  
**sudo yum groupinstall "Development Tools"**  
**sudo yum install gettext-devel openssl-devel perl-CPAN perl-devel autoconf zlib-devel libcurl-devel expat-devel**  
После получаем ссылку на свежий релиз git c github.com  
https://github.com/git/git/archive/refs/tags/v2.32.0.tar.gz  
Качаем архив  
**wget https://github.com/git/git/archive/refs/tags/v2.32.0.tar.gz**  
Распаковываем  
**tar -zxf v2.32.0.tar.gz**  
Переходим в папку с распакованным архивом  
**cd git-2.32.0**  
Генерируем скрипт configure  
**make configure**  
С помощью скрипта выполянем предварительную проверку зависимостей ПО и аппаратных конфигураций  
**./configure --prefix=/usr/local**  
С помощью -prefix=/usr/local объявляем целевую папку размещения нового бинарного файла.  
Устанавливаем  
**sudo make install**  
Git установлен.  
Проверим версию  
**[admin@devops git-2.32.0]$ git --version**  
**git version 2.32.0**  
Проверим работосопобность, склонировав репозиторий.  
**git clone https://github.com/it763/quantori.git**  
  
**[admin@devops ~]$ git clone https://github.com/it763/quantori.git  
Cloning into 'quantori'...  
remote: Enumerating objects: 158, done.  
remote: Counting objects: 100% (158/158), done.  
remote: Compressing objects: 100% (157/157), done.  
remote: Total 158 (delta 91), reused 0 (delta 0), pack-reused 0  
Receiving objects: 100% (158/158), 19.29 MiB | 2.43 MiB/s, done.  
Resolving deltas: 100% (91/91), done.**  

