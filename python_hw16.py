#Написать программу, которая будет считывать из файла gps координаты,
#и формировать текстовое описание объекта и ссылку на google maps.
#Пример:

#Input data: 60,01';30,19'
#Output data:
#Location: Теремок, Енотаевская улица, Удельная, округ Светлановское, Выборгский район, Санкт-Петербург, Северо-Западный федеральный округ, 194017, РФ
#Goggle Maps URL: https://www.google.com/maps/search/?api=1&query=60.016666666666666,30.322


from geopy.geocoders import Nominatim

with open('coordinates.txt','r') as in_file:
    coord_raw=in_file.readline()
coord=[i.rstrip("'") for i in coord_raw.split(';')]
coord=[i.replace(",",".") for i in coord]                 #Преобразование записи координат читаемому geopy виду

geolocator = Nominatim(user_agent="app1")
location = geolocator.reverse(coord)        #Принимает в качестве аргументов координаты и по ним выдает описание геопозиции
print('Location: ', location.address)


ref= f'https://www.google.com/maps/search/?api=1&query={coord[0]},{coord[1]}'
print ('Goggle Maps URL: ',ref)


