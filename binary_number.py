binary_number = int(input("Enter binary number: "))
counter = 2

while binary_number > 0:
	digit = binary_number % 10
	binary_number = (binary_number - digit) // 10
	counter *= 2
	decimal_digit = digit * counter
	decimal_digit += decimal_digit
	
	
	print("", decimal_digit)
