
def month_to_season(n):
    
    if (n == 12) or (n == 1) or (n == 2):
        return "Зима"
    if (n == 3) or (n == 4) or (n == 5):
        return "Весна"
    if (n == 6) or (n == 7) or (n == 8):
        return "Лето"
    if (n == 9) or (n == 10) or (n == 11):
        return "Осень"
    
for month in range(1,13):
    print(month_to_season(month))
  
    
    
