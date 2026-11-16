counter = 0
passes = 0

while counter >= 0:
    first_input = int(input("Enter 1 0r 2: "))
    if first_input == 1 or first_input == 2 :
        passes += 1
        print("The total number of failures is", counter, "and the total number of passes is", passes)
        break
    else:
        counter += 1
    
    
