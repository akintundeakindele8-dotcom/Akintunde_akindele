price = float(input("Enter price in dollars: "))
money = float(input("Enter amount paid in dollars: "))
change = money - price

while change > 0:
	if change > 1:
		quater = change // 25
		change -= quater
	if change > 0.9:
		dime = change // 10 
		change -= dime 
	if change > 0.01:
		penny = change // 1
		change -= penny	
	print("", quater, "quaters", "", dime, "dimes",  "", penny, "pennies") 