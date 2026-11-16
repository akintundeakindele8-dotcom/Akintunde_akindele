principle = int(input("Enter your saved amount or enter -1 to quit computing : "))

while principle != -1:
		principle = int(input("Enter your saved amount or enter -1 to quit computing : "))
		for year in range(1, 31):
			accululated_interest = principle * (1 + 7/100)**year
			accululated_interest =+ accululated_interest 
			print(f"{year}  {accululated_interest}")
			
			if principle == -1:
				break
if principle == -1:
	print("No values entered")
	

	
