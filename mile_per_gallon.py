counter = 0
total_mile_gallon = 0
gallon = float(input("Enter amount of gallons or -1 to quit: "))	
while gallon != -1:
	mile = int(input("Enter amount of miles: "))
	
	mile += mile
	gallon += gallon
	counter += 1
	mile_gallon = mile /gallon
	total_mile_gallon += mile_gallon
	print("The mile/gallon for this tank is:", mile_gallon)
	gallon = float(input("Enter amount of gallons or -1 to quit: "))
if counter != 0:
	average = total_mile_gallon / counter
	print("After", counter, "trips, the tanks used an average of", average,"miles/gallon")
	
	
else:
	print("No value inputted")
