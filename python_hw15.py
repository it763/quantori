import ipaddress
class router:
    '''
    router- класс, имитируюзий работу маршрутизатора.
    Имеет методы добавления/отображения/удаления ip интерфейсов и записей таблицы маршрутизации.
    Просмотр списка интерфейсов:
    r.sh_ip_int()

    Добавление ip интерфейса:
    r.add_int(interface,address)
    Нужно указать имя интерфейса и его ip адрес в виде ip/prefix
    При добавлении интерфейса добавляется маршрут к непосредственно подключенной к этому интерфейсу сети
    Пример:
    r.add_int('eth0','192.168.0.1/24')

    Удаление ip интерфейса:
    no_ip_int(interface)
    Нужно указать имя интерфейса
    Пример:
    r.no_ip_int('eth0')
    Удаляет интерфейс eth0, вместе с ним маршрут к непосредственно подключенной сети через этот интерфейс.

    Просмотр таблицы маршрутизации:
    r.sh_ip_route()

    Добавление маршрута в таблицу маршрутизации:
    ip_route_add(network,gate)
    Нужно указать адрес сети в виде network/prefix и адрес шлюза, через который доступна подсеть
    Пример:
    r.ip_route_add('192.168.5.0/24','192.168.1.10')
    Маршрут будет добавлен, если в таблице маршрутизации имеется маршрут к шлюзу.

    Удаление маршрута:
    r.ip_route_del(network)
    Нужно указать сеть, к которой удаляется маршрут в виде network/prefix
    Пример:
    r.ip_route_del('192.168.5.0/24')
    '''
    def __init__(self):
        self.ip_int={}                                #Словарь интерфейс:ip адрес
        self.ip_routes={}                             #Словарь сеть:адрес шлюза

    def add_int(self,interface,address):              #Добавить интерфейс с ip адресом. Требуется ввести данные вида адрес/маска, например 192.168.1.1/24
        self.ip_int[interface]=ipaddress.ip_interface(address)
        print(f'Interface {interface} assigned address {address}')
        self.ip_routes[self.ip_int[interface].network]=self.ip_int[interface].ip  #Добавляется маршрут к непосредственно подключенной сети


    def sh_ip_int(self):                              #Вывести список интерфейсов и их ip адресов
        print('Network interfaces list: ')
        for k,v in self.ip_int.items():
            print (k,': ',v.compressed)

    def no_ip_int(self,interface):                     #Удалить интерфейс
         if interface in self.ip_int.keys():
             del self.ip_routes[self.ip_int[interface].network]  #Удаляется маршрут к непосредственно подключенной сети
             del self.ip_int[interface]                                     #Удаляется интерфейс

             print(f'Interface {interface} was deleted')
         else:
             print('Router has no such interface')

    def sh_ip_route(self):                               #Просмотр таблицы маршрутизации
        print('Routing table: ')
        for k,v in self.ip_routes.items():
            print(k.compressed,' via ',v.compressed)


    def ip_route_add(self,network,gate):          #Добавление маршрута в таблицу маршрутизации
        gate_ip=ipaddress.ip_address(gate)        #Получаем ip адрес шлюза
        net_ip=ipaddress.ip_network(network)      #Получаем ip адрес сети
        route_present=0
        for n in self.ip_routes.keys():           #Проверка наличия маршрута к указанному шлюза в таблице маршрутизации
            if gate_ip in n:
                route_present+=1
            else:
                pass
        if route_present:
            self.ip_routes[net_ip] = gate_ip       #Внесение записи в таблицу маршрутизации
            print(f'Route to {net_ip.compressed} via {gate_ip.compressed} was added')
        else:
            print(f'Gate {gate_ip.compressed} is not available')


    def ip_route_del(self,network):               #Удаление маршрута из таблицы маршрутизации
        net_ip = ipaddress.ip_network(network)
        if net_ip in self.ip_routes.keys():       #Проверка наличия маршрута в таблице маршрутизации
            del self.ip_routes[net_ip]
            print(f'Route to {net_ip.compressed} was deleted')
        else:
            print('No such route')


r1=router()



r1.add_int('eth0','192.168.0.1/24')
r1.add_int('eth1','192.168.1.1/24')

#r1.sh_ip_route()
#r1.no_ip_int('eth0')
#r1.sh_ip_int()
#r1.sh_ip_route()
#r1.ip_route_add('192.168.5.0/24','192.168.10.10')
#r1.sh_ip_route()
#r1.ip_route_del('192.168.5.0/24')
#r1.sh_ip_route()

