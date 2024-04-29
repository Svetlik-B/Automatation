# Напишите цикл, который печатает весь каталог (список) в формате <марка> - <модель>. <номер телефона>.

from smartphone import Smartphone


smartphone_1 = Smartphone("Xiaomi", "Redmi", "+79000000000")
smartphone_2 = Smartphone("Samsung", "Galaxy", "+79999999999")
smartphone_3 = Smartphone("Iphone", "ProMax", "+79888888888")
smartphone_4 = Smartphone("phone", "Max", "+79088888880")
smartphone_5 = Smartphone("mi", "Red", "+79000000999") 


catalog = [smartphone_1, smartphone_2, smartphone_3,smartphone_4, smartphone_5]


for phone in catalog:
    print(phone.brand, "-",phone.model, ".", phone.number)
    # phone.sayPhone()
    # print(phone.phone_b)
    # phone.sayNumber()
    # sayNumber(phone)
    # phone.sayHello(False)
