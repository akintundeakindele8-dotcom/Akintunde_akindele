
number = int(input("Enter an integar: "))

while number > 0:
	last_digit = number % 10
	number = (number - last_digit) // 10
	
	print(last_digit, end = " ")
	
		
