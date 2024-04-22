# Создайте файл lesson_3_task_3.py.
# Импортируйте классы Address и Mailing.
# В файле создайте экземпляр класса Mailing.
# Заполните поля класса адресами (to_address и from_address), трек-номером (track) и стоимостью (cost).
# Распечатайте в консоль отправление в формате: 
# Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в
# <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.


from address import Address
from mailing import Mailing
 
 
to_address = Address("333222", "Саратов", "улица Карла Маркса", "123", "1") 
from_address = Address("444555", "Сарапул", "улица Максима Горького", "321", "3")
mailing1 = Mailing(to_address, from_address, "1000", "123456")


print(mailing1)


# решение 2
# print(
# "Отправление ", mailing1.track, " из ",  mailing1.from_address.index,", ",
# mailing1.from_address.city,", ", mailing1.from_address.street, ", ",
# mailing1.from_address.house, " - ", mailing1.from_address.apartment, " в ",
# mailing1.to_address.index, ", ", mailing1.to_address.city, ", ",
# mailing1.to_address.street, ", ", mailing1.to_address.house, " - ", mailing1.to_address.apartment,
# ". Стоимость ", mailing1.cost, " рублей.",
# sep=""
# )

# решение 3
# def printAdress(address):
#     print(
#          address.index,", ",
#          address.city,", ", address.street, ", ",
#          address.house, " - ", address.apartment,
#          sep="", end=""
# )
# 
# print("Отправление", mailing1.track, "из", end=" ")
# printAdress(from_address)
# print(" в ", end="")
# printAdress(to_address)
# print(". Стоимость ", mailing1.cost, " рублей.", sep="")

# решение 4
# print(
#     "Отправление ", mailing1.track, " из ",
#     str(from_address), " в ", str(to_address),
#     ". Стоимость ", mailing1.cost, " рублей.", 
#     sep=""
# )


