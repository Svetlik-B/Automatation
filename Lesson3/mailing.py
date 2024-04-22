
# В отдельном файле создайте класс Mailing (почтовое отправление).


class Mailing: 
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
        
    def __str__(self):
        result  = "Отправление " +  self.track + " "
        result += "из " + str(self.from_address) + " "
        result += "в " + str(self.to_address) + ". "
        result += "Стоимость " + self.cost + " рублей."  
        return result
    
    