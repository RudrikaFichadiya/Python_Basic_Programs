print("Hello World!")  # will print hello world

name = 'Demo in Python using PyCharm'  # we are storing string
print(name)
name = 15  # can store numbers
print('5+2=', 5 + 2)  # will print the result of addition operation
print ("Hello! First Sample Program in Python") # will print given string
print("_________________________________________________________________________________")
print("Different airithmetic operations")
print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 % 2 =", 5%2)
print("5 ** 2 =", 5**2) # will return power like, 5^2
print("5 // 2 =", 5//2) # will print floor value after divide operation
print("_________________________________________________________________________________")
print("Single and Multiline String")
quote = "\"Always remember you are unique"
multiline_quote = '''this is multiline
quote demo'''
print("%s %s %s" %('Quote concatanation', quote, multiline_quote))
print("_________________________________________________________________________________")
print("List in Python")
language_list = ['C', 'C++', 'Java', 'Lisp', 'Python']
print("First Item in List =", language_list[0]) # access first item using index
language_list[0]="COBOL" #replace first item with new value
print("First Item in List after modification =", language_list[0])
print("\n_______________________Demo of user defined function_________________________")
def add(num1, num2):
    print( num1 + num2 )

add(1,2)
print("\n_____________________Demo of for loop to find prime number_____________________")
for i in range(2,30):
    j=2
    counter = 0
    while j<i:
        if i%j == 0:
            counter = 1
            j=j+1
        else:
            j=j+1
    if counter == 0:
        print(str(i)+ " is a prime number")

    else:
        counter = 0
print("_________________________________________________________________________________")
# program to implement lists and different operations of it
print("___program to implement lists and different operations of it____")
favsong_list = ['The way I am', 'A different way', 'Pray for me', 'Attention']
favmovies_list = ['Inception', 'Source Code', 'Lucy', 'Noah']
favorites= favsong_list + favmovies_list  # combining two lists
favorites.append('Because Every Raindrop is a HOPE') # appending new item in existing list
print("Favorite Songs + Favorite Movies + Favorite Book")
print(favorites)
print("_________________________________________________________________________________")
print("\nThere is 20 person in one bus. 10 getoff, 3 came in, 15 came in, 5 getoff... There are different 3 more buses having 15 people throughout the bus ride then write one line equation for count how many people are there during the bus ride")

print("Solution in one line of complex problem definition")
print("20-10+3+15-5+(3*15)=", eval('20-10+3+15-5+(3*15)'))

# Program to create simple arithmetic calculator
print("Simple arithmetic calculator")
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def div(num1,num2):
    return num1/num2
print("_________________________________________________________________________________")
print("This is the simple arithmetic cal-c")

print(" 1. Addition of two numbers \n 2. Subtraction of two numbers \n 3. Multiplication of two numbers \n 4. Division of two numbers \n 5. Power")
choice = input("Enter your choice(1/2/3/4)=")
num11 = int(input("Enter first number="))
num22 = int(input("Enter second number="))

if choice == '1':
    print(num11, "+",num22, "=", add(num11,num22))
elif choice == '2':
    print(num11, "-", num22, "=", sub(num11,num22))
elif choice == '3':
    print(num11, "*", num22, "=", mul(num11,num22))
elif choice == '4':
    print(num11, "/", num22, "=", div(num11,num22))
else:
    print("Enter valid choice...!")



