2.1
x = 2
y = 3
print("Value of x is ", x)

print('Value of', x, '+', x, 'is', (x + x))

print('x =')

print((x + y), '=', (y + x))

2.2
rating = input(int("Enter an integer rating between 1 and 10"))

2.3
grade = 91
if grade >= 90:
    print("Congratulations! Your grade of", grade, "earns you an A in this course")
    
2.4
value = 27.5
print(value + 2)
print(value - 2)
print(value * 2)
print(value / 2)
print(value // 2)
print(value ** 2)

2.5
r = 2
pie = 3.14259
diameter = 2 * r
area = r * r
circumference = 2 * pie * r
print("Area is ", area)
print("Diameter is ", diameter)
print("Circumference is ", circumference)

2.6
value = input("Enter a number: ")
value = int(value)
if value % 2 == 0:
    print(" ", value, "is an even number")
    
if value % 2 != 0:
    print(" ", value, "is an odd number")



2.7
Value1 = 1024
value2 = 2
if 1024 % 4 == 0:
    print("1024 is a multiple of 4")
if 2 % 10 != 0:
    print("2 is not a multiple of 10")
 
 
 
2.8
input(int("Enter any number"))
int = value
square = value * value
cube = value * value * value
print("")

2.9
value1 = ord('A')
value2 = ord('B')
value3 = ord('C')
value4 = ord('D')
value5 = ord('b')
value6 = ord('c')
value7 = ord('d')
value8 = ord('0')
value9 = ord('1')
value0 = ord('2')
value11 = ord('3')
value12 = ord('$')
value13 = ord('*')
value14 = ord('+')
value16 = ord(' ')
print("B is",  value2, "C is ", value3, "D is ", value4, "b is ", value5, "c is ", value6, "d is ", value7, "0 is ", value8, "1 is ", value9, "2 is ", value0, "3 is ", value11, "$ is ", value12, "* is ", value13, "+ is ", value14, "  is ", value16 )


2.10
value1 = input("Enter first value: ")
value1 = int(value1)
value2 = input("Enter second value: ")
value2 = int(value2)
value3 = input("Enter third value: ")
value3 = int(value3)

sum = value1 + value2 + value3
average = (value1 + value2 + value3) / 3
product = value1 * value2 * value3
print("The sum of the values is", sum)
print("The product of the values is", product)
print("The average of the values is", average)

minimum = value1
if minimum > value2:
    minimum = value2
if minimum > value3:
    minimum = value3
if minimum == value2 and value3:
    print("There is no smallest number")
maximum = value1
if maximum > value2:
   maximum = value2
if value2 > value3:
   maximum = value2
if minimum == value2 and value3:
   print("There is no largest number")
   
   
print("", minimum, "is the smallest number")
print("", maximum, "is the Largest number")


2.11
numb1 = input("Enter five digit number: ")
numb1 = int(numb1)
first_number = numb1 / 10000
rem1 = numb1 % 10000
second_number = rem1 / 1000
rem2 = rem1 % 1000
third_number = rem2 / 100
rem3 = rem2 % 100
fourth_number = rem3 / 10
rem4 = rem2 % 10
fifth_number = rem4 / 1
first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)
fourth_number = int(fourth_number)
fifth_number = int(fifth_number)

print("", first_number, "", second_number, "", third_number, "", fourth_number, "", fifth_number)
 
 
2.12
inv = 1000
inv = int(inv)
tenth_year = inv * 1.07**10
twentieth_year = tenth_year * 1.07**20
Thirtheth_year = twentieth_year * 1.07**30
tenth_year = float(tenth_year)
twentieth_year = float(twentieth_year)
Thirtheth_year = float(Thirtheth_year)

print("After 10 years you will have", tenth_year, "After 20 years you will have", twentieth_year, "After 30 years you will have", Thirtheth_year, )


2.13
numb1 = input("Enter any number: ")
numb1 = int(numb1)
exponent = numb1 ** numb1
print("", numb1, "raised to the power of", numb1, "is", exponent)

2.14
age = input("Enter your real age: ")
age = int(age)
maxheart_rate = 220 - age
print("Your maximum heart rate is", maxheart_rate)
lowertarget_heartrate = maxheart_rate * 0.5
highertarget_heartrate = maxheart_rate * 0.85

print("Your heart rate should be between", lowertarget_heartrate, "and", highertarget_heartrate)

2.15
numb1 = input("Enter the first decimal number: ")
numb1 = float(numb1)
numb2 = input("Enter the second decimal number: ")
numb2 = float(numb2)
numb3 = input("Enter the third decimal number: ")
numb3 = float(numb3)

if numb1> numb2 and numb2 > numb3 :
    print("", numb1, numb2, numb3 )
if numb1> numb3 and numb3 > numb2 :
    print("", numb1, numb3, numb2 )
if numb2> numb1 and numb1 > numb3 :
    print("", numb2, numb1, numb3 )
if numb2> numb3 and numb3 > numb1 :
    print("", numb2, numb3, numb1 )
if numb3> numb1 and numb1 > numb2 :
    print("", numb3, numb1, numb2 )    
if numb3> numb2 and numb2 > numb1 :
    print("", numb3, numb2, numb1 )
    
if numb3 == numb2 and numb2 > numb1 :
    print("", numb3, ("="), numb2, (""), numb1 )    

if numb1 == numb2 and numb2 > numb3 :
    print("", numb1, ("="), numb2, (""), numb3  )

if numb1 == numb3 and numb3 > numb2 :
    print("", numb3, ("="), numb1, (""), numb2  )
    
if numb3 == numb2 and numb1 > numb2 :
    print((""), numb1, "", numb3, ("="), numb2)    

if numb1 == numb2 and numb3 > numb2 :
    print("", numb3, "", numb1, ("="), numb2)

if numb1 == numb3 and numb2 > numb3 :
    print("", numb2, "", numb3, "=", numb1)
    
if numb1 == numb2 and numb2 == numb3 :
    print("", numb1, numb2, numb3, ("are all equal") )




