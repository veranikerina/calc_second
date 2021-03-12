str_command = input ("Please type command a + b or a - b: ").replace(' ','')

type_A = ''
str_A = ''

type_B = ''
str_B = ''

operation = ''
i = 0

while i < len(str_command) :
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^':
        if str_A == '':
            type_A = str_command[i]
        elif operation != '':
            type_B = str_command[i]
        else:
            operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B += str_command[i]
    i += 1

delimoe = float(type_A + str_A)
delitel = float(type_B + str_B)

result = None

if operation == '/':
    if delitel == 0:
        result = 'Inf'
    else:
        result = delimoe / delitel
elif operation == '+':
    result = delimoe + delitel
elif operation == '-':
    result = delimoe - delitel
elif operation == '*':
    result = delimoe * delitel
elif operation == '^':
    result = delimoe ** delitel
else:
    result = "unknown"

print("Result: " + str(result))
