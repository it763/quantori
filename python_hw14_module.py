class Employee:                                  #Заводим новый класс Emloyee
  def __init__(self,name,phone,salary=10000):    #__init__ - метод инициализации класса
    self.name = name                             #Задаем параметры для объекта класса
    self.phone = phone
    self.salary = salary
  def print_salary_info(self):                   #Объявляем метод класса. Вывод информации об объекте
    print("Employee {} gets {} Rubles".format(self.name,self.salary))
  def add_salary(self,delta=5000):               #Объявляем метод класса. Изменение размера ЗП
    self.salary = int(self.salary)+delta

