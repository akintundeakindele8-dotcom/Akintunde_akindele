counter = 1
sum = 0
product =1
min = 0
max = 0
while counter <= 4:
	number = int(input("Enter a number: "))
	sum = sum + number
	product = product * number
	counter += 1
	if min < number :
		min = number
	if number > max:
		max = number	

average = sum / counter
print("The sum is", sum, ",the product is", product, "and the average is\n", average, "and the min and max are", min, max, "respectively")
	
