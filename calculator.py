print ("Welcome to the Python Calculator")
print ("")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponent(x, y):
    return x ** y

print ("Select operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Exponent")

choice = input("Enter choice: (1/2/3/4/5):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print(num1,"+",num2,"=", add(num1,num2))
elif choice == "2":
    print (num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice == "5":
    print(num1,"**",num2,"=", exponent(num1,num2))
else:
   print("Invalid input")

#peepee poopoo