from socket import *
#База данных DNS  в виде словаря. Предопеределены несколько записей
dns_db={'google.com':'64.233.164.138','yandex.ru':'77.88.55.80','domain.name':'127.0.0.1'}

#Определяем параметры сервера
host = 'localhost'
port = 53
addr = (host,port)
#socket - функция создания сокета
#первый параметр socket_family может быть AF_INET или AF_UNIX
#второй параметр socket_type может быть SOCK_STREAM(для TCP) или SOCK_DGRAM(для UDP)
udp_socket = socket(AF_INET, SOCK_DGRAM)   #создаем UDP сокет
#bind - связывает адрес и порт с сокетом
udp_socket.bind(addr)    #Начинаем слушать сокет

while True:

    print('Waiting for requests...')

    # recvfrom - получаем UDP сообщения
    conn, addr = udp_socket.recvfrom(1024)
    print('client addr: ', addr)                                     #info Пишем сокет, с которого получено сообщение
    print('Received message: ',bytes.decode(conn))                   #info Текст входящего запроса
    if 'ADD ' in bytes.decode(conn):                                 #Если во входящем соообшении есть подстрока 'ADD ', значит пришел запрос на добавление записи.
        new_entry_list=bytes.decode(conn).split()[1].split(':')      #Преборазоваваем входящее сообщение, получаем из него hostname и ip address
        new_hostname=new_entry_list[0]
        new_ip_addr=new_entry_list[1]
        dns_db[new_hostname]=new_ip_addr                             #Добавление новой записи в бд dns
        udp_socket.sendto(str.encode('New entry was added'), addr)   #Отправка клиенту сообщения о добавлении новой записи
    elif str(bytes.decode(conn)) in dns_db.keys():                   #Получаем запрос с hostname, если такой есть в бд, отправляем значение ip
        answer = dns_db[bytes.decode(conn)]
        udp_socket.sendto(str.encode(answer), addr)
    else:
        udp_socket.sendto(str.encode('No such entry'), addr)         #иначе пишем что такая запись отсутствует


#udp_socket.close()