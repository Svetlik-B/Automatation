percentage = 0.1

def bank(x, y):
    summ = x
    for _ in range(0, y):
        summ = summ + summ * percentage
    return summ

result = bank(x=100, y=2)

процент = 0.1
сумма = 100

# после первого года
сумма = сумма + сумма * процент # 110
print("после первого года:", сумма)

# после второго года
сумма +=  сумма * процент
print("после второго года:", сумма)


def b(сумма = 100, процент: any = 0.1):
    print(сумма, процент)
    



















