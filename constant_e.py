number = int(input("Enter a denominator value: "))
CONSTANT = 1
total = 0
product = 1

for counter in range(number, 0, -1):
		product *= number
		
		e = CONSTANT + ( CONSTANT  / (product))
		total += e
print("total is ", total)
