#Напишите функцию, которая переводит значения показаний
#температуры из Цельсия в Фаренгейт и наоборот.
#Формулы вычисления для перевода из одной системы в другую:
#(0 °C × 9/5) + 32 = 32 °F
#(32 °F − 32) × 5/9 = 0 °C

#Функция принимает на вход значение температуры с указаением единици измерения C или F.
#Принимаются варианты C,c,F,f.
#В результате функция выводит значение температуры в другой системе измерения.
def translate(in_val):
    in_list=list(in_val)

    if in_list[-1].lower() == 'c':
        out_val = int(''.join(in_list[:-1]))*(9/5)+32
        return out_val
    elif in_list[-1].lower() == 'f':
        out_val = (int(''.join(in_list[:-1])) -32)*(5/9)
        return out_val
    else:
        print('Введите корректные данные с указанием единицы измерения')


a=translate('20C')
print(a)