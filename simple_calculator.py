#simple calculator
signs = ["+", "-", "*", "/"]

print("Usable operators:")
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")

def get_operators(): 
    while True:
        operator = input("Choose an operator: ")
        if operator in signs:
            return operator
        else:
            print("Please enter a valid operator (+, -, *, /)")

def get_digits():       
    try:
        first_num = float(input("Your first number: "))
        sec_num = float(input("Your second number: "))
        return first_num, sec_num 
    except ValueError:
        print("That's not a valid number! Please enter digits only.")
        return None, None

def cal(operator, digits):
    first_num, sec_num = digits

    if first_num is None or sec_num is None:
        return  

    if operator == "+":
        result = first_num + sec_num
    elif operator == "-":
        result = first_num - sec_num
    elif operator == "*":
        result = first_num * sec_num
    elif operator == "/":
        if sec_num != 0:
            result = first_num / sec_num
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Unknown operator.")
        return

    print(f"Result of {first_num} {operator} {sec_num} = {result}")

# 🔁 Main Loop
while True:
    operator = get_operators()
    digits = get_digits()
    cal(operator, digits)

    play_again = input("DO U WANNA RECALCULATE??? (y/n): ").lower()
    if play_again != 'y':
        print("STUDY MY FRIEND!")
        break
