#Tenth day challenge
#Calculator

print("Welcome to calculator !!!")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = float(input("What is the first number?\n"))

for operator in operations:
    print(operator)

operator = input("Choose an operator\n")
num2 = float(input("What is the second number?\n"))
answer = operations[operator](num1, num2)

print(f"{num1} {operator} {num2} = {answer}")

while True:
    ask = input(f"Type yes to continue calculating with {answer} or no to exit\n").lower()
    if ask == "no":
        break
    else:
        operator = input("Choose an operator\n")
        num2 = float(input("What is the second number?\n"))
        previous_answer = answer
        answer = operations[operator](previous_answer, num2)
        print(f"{previous_answer} {operator} {num2} = {answer}")