number= int(input("Enter a number to find the factorial: "))
product = 1
for number in range(number, 1, -1):
	product *= number
	print(f"{product}")
	
	
