number = int(input("Enter a palindrome: "))
reverse_number = 0
while number > 0:
    last_digit = number % 10
    reverse_number =  (reverse_number* 10) + last_digit
    #reverse_number = (last_digit * 10) 
    number = (number - last_digit ) // 10
    
if number == reverse_number:
    print("", reverse_number, "is a palindrome")
else:
    print("", reverse_number, "is a not palindrome")
