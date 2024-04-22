# Список объектов
# Создайте файл smartphone.py.
# В файле объявите класс 
# Smartphone.
# Объявите в классе конструктор.

class Smartphone:
    def __init__(self, phone_brand, phone_model, phone_number):
        self.brand = phone_brand
        self.model = phone_model
        self.number = phone_number
    
    
    def sayBrand(self):
        print("марка телефона: ", self.brand)
        
    
    def sayModel(self):
        print("модель телефона: ",  self.model)
        
    
    def sayNumber(self):
        print("номер телефона: ", self.number)
        
        
    def sayPhone(self):
        print(self.brand, "-",self.model, ".", self.number)
        
        
    # def sayHello(self, word):
        # print(word, self.model)