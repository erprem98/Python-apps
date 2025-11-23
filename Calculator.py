def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multi(x,y):
    return x * y

def division(x,y):
    return x // y

print("Select operations from below")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divison")

while True:
    choice = input("Enter your choice from these 1/2/3/4: ")
    if choice in ('1','2','3','4'):
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter Second number: "))
        except ValueError:
            print("Wrong input")
            continue
        if choice == '1':
            print(f"Addition of {num1} and {num2} is ",add(num1,num2))
        elif choice == '2':
            print(f"Substraction of {num1} and {num2} is ",substract(num1,num2))
        elif choice == '3':
            print(f"Multiplication of {num1} and {num2} is ",multi(num1,num2))    
        elif choice == '4':
            print(f"Divison of {num1} and {num2} is ",division(num1,num2))
        next_calculation= input("Do you want for further calcualtion (no/yes) \n")  
        if next_calculation == 'no':
            break
    else:
        print("Invalid choice")    