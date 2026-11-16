binary_number = int(input("Enter binary number"))
while binary_number > 0:
	digit = binary_number % 10
	binary_number = binary_number // 10
	number = (digit*10) + binary_number
print(binary_number )
