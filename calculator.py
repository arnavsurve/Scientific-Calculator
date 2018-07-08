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

def root(x, y):
    return x ** (1/y)

print ("Select operation:")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("5. Exponent")
print ("6. Root")

choice = input("Enter choice: (1/2/3/4/5/6):")

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
elif choice == "6":
    print(num2,"\/`",num1,"=", root(num1,num2))
else:
   print("Invalid input")

