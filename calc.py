input_str = input ("Please type command: ")

operation = '+'
true = False
str_A = ''
result = 0

for letter in input_str:
    if letter in "0123456789":
        true = True
    if letter in "+ - * / ^" and true:
        delitel = float(str_A)
        if operation == '/':
            if delitel == 0:
                result = 'Inf'
            else:
                result = result / delitel
        elif operation == "+":
                result = result + delitel
        elif operation == "*":
                result = result * delitel
        elif operation == "-":
                result = result - delitel
        elif operation == "^":
                result = result ** delitel
        else:
                result = None
        operation = letter
        true = False
        str_A = ''
    else:
        str_A += letter

delitel = float(str_A)
if operation == '/':
    if delitel == 0:
        result = 'Inf'
    else:
        result = result / delitel
elif operation == '+':
    result = result + delitel
elif operation == '-':
    result = result - delitel
elif operation == '*':
    result = result * delitel
elif operation == '^':
    result = result ** delitel
else:
    result = "unknown"

print("Result: " + str(result))
