#pip install exif
#https://pypi.org/project/exif/
from geopy.geocoders import Nominatim
from exif import Image
with open('img.jpg', 'rb') as image_file:
    my_image = Image(image_file)                                 #Открываем изображение

if my_image.has_exif:   #Получаем координаты gps и приводим их к виду, в котором принимает на вход программа из 16 HW
    gps_latitude_list=str(my_image.gps_latitude).lstrip('(').rstrip(')').split(', ')
    gps_longitude_list=str(my_image.gps_longitude).lstrip('(').rstrip(')').split(', ')
    gps_latitude= float(gps_latitude_list[0])+float(gps_latitude_list[1])/60+float(gps_latitude_list[2])/3600
    gps_longitude=float(gps_longitude_list[0])+float(gps_longitude_list[1])/60+float(gps_longitude_list[2])/3600
    output_coord=str(gps_latitude).replace('.',',')+str("'")+str(';')+str(gps_longitude).replace('.',',')+str("'")
    with open('coordinates17.txt','w') as out_file:
        out_file.write(output_coord)                #Записываем координаты в файл
else:
    print('Image has no exif info')

#На выходе получаем файл с координатами. Передаем его на вход программе из HW16
with open('coordinates17.txt','r') as in_file:
    coord_raw=in_file.readline()
coord=[i.rstrip("'") for i in coord_raw.split(';')]
coord=[i.replace(",",".") for i in coord]                 #Преобразование записи координат читаемому geopy виду

geolocator = Nominatim(user_agent="app1")
location = geolocator.reverse(coord)        #Принимает в качестве аргументов координаты и по ним выдает описание геопозиции
print('Location: ', location.address)


ref= f'https://www.google.com/maps/search/?api=1&query={coord[0]},{coord[1]}'
print ('Goggle Maps URL: ',ref)