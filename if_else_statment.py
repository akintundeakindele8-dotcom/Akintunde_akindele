print("Enter two integers, and I will tell you, the relationships they satisfy.")
number1 = int(input('Enter first integer: '))
number2 = int(input('Enter second integer: '))
if number1 < number2:
    print("", number1, "less than", number2)
else:
    print("", number1, "greater than", number2)
    
if number1 == number2:
    print("", number1, "is equal to", number2)
else:
    print("", number1, "is not equal to", number2)
if number2 < number1:
    print("", number2, "less than", number1)
else:
    print("", number2, "greater than", number1)
    
    
