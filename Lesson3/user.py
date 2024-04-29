# Создание класса
# Создайте файл user.py.
# В файле объявите класс User. 
# Объявите в классе конструктор.


class User:
    
    def __init__(self, first_name, last_name):
        print("Я создался")
        self.f_name = first_name
        self.l_name = last_name
    
    
    def sayName(self):
        print("меня зовут ", self.f_name)
        
    
    def sayLname(self):
         print("моя фамилия ", self.l_name)
    
    
    def fullName(self):
        print("полное имя ", self.f_name, self.l_name)
    
    
      
# alex = User("Alex", "Ivanov")
# alex.sayName()
# alex.sayLname()
# alex.fullName()