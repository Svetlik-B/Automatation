def fizz_buzz(n): 
    for num in range(1, n + 1):
        isSpeciaCase = False
        if num % 3 == 0:
            print("Fizz", end = "")
            isSpeciaCase = True
        if num % 5 == 0:
            print("Buzz", end = "")
            isSpeciaCase = True
        if isSpeciaCase:
            print()
        else:
            print(num)
fizz_buzz(17)
