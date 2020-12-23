import art

print(art.logo)


num_a = float(input("What's the first number?: "))
print("+")
print("-")
print("*")
print("/")
operator = input("Pick an operation: ")
num_b = float(input("What's the second number?: "))


def add(num_a, num_b):
    return num_a + num_b


def sub(num_a, num_b):
    return num_a - num_b


def mul(num_a, num_b):
    return num_a * num_b


def div(num_a, num_b):
    return num_a / num_b


ans_wer = 0


finished = False

while not finished:
    if operator == "+":
        ans_wer = add(num_a, num_b)
        print(f"{num_a} {operator} {num_b} = {ans_wer}")
    elif operator == "-":
        ans_wer = sub(num_a, num_b)
        print(f"{num_a} {operator} {num_b} = {ans_wer}")
    elif operator == "*":
        ans_wer = mul(num_a, num_b)
        print(f"{num_a} {operator} {num_b} = {ans_wer}")
    elif operator == "/":
        ans_wer = div(num_a, num_b)
        print(f"{num_a} {operator} {num_b} = {ans_wer}")

    cont = input(f"Type 'y' to continue calculation with {ans_wer}, or type 'n' to start a new calculation: ")

    if cont == "y":
        operator = input("Pick an operation: ")
        num_b = float(input("What's the next number?: "))
        num_a = ans_wer
    elif cont == "n":
        num_a = float(input("What's the first number?: "))
        print("+")
        print("-")
        print("*")
        print("/")
        operator = input("Pick an operation: ")
        num_b = float(input("What's the second number?: "))
