while True:
    numbers = [1,3,9,12,16,99]
    x = int(input("Fill a number? "))
    y = numbers.index(x)
   
    if x in numbers:
        print(y)
    else:
        print("The number is not in the list")