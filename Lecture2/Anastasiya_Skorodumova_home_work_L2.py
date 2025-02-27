# Homework 2.1.
# print('homework 2.1')
# It's time to complicate the code -
# let's find the largest of four numbers.
# input()|int() or float() < > == <= >= if/elif/else type() comments!!!#####
print('homework 2.1')
number1 = int(input('number 1: '))
number2 = int(input('number 2: '))
number3 = int(input('number 3: '))
number4 = int(input('number 4: '))
print("Input numbers: ", number1, number2, number3, number4)
print(".........Search MAX element......")
max_=0
if number1 > number2:
    print(number1, '>',number2)
    max12 = number1
else:
    print(number1, '<',number2)
    max12 = number2
    
if number2 < number3:
    print(number2, '<',number3)
    max23 = number3
else:
    print(number2, '>',number3)
    max23 = number2
    
if number3 > number4:
    print(number3, '>',number4)
    max34 = number3
else:
    print(number3, '<',number4)
    max34 = number4

if max12 > max23:
    print('MAX element = ', max12)
else:
    if max23>max34:
        print('MAX element = ', max23)
    else:
        print('MAX element = ', max34)




# Homework 2.4.
#  "one Mississippi, two Mississippi, three Mississippi"
# "Ready or not, here I come!"
print('\nhomework 2.4')
import time

for i in range(1,6):
    print(i, "Mississippi")
    time.sleep(1)
print('Ready or not, here I come!')

# Homework 2.6.
#  calculator with loop +-/*
print('\nhomework 2.6')

num1 = input('Put integer or float number:')
num2 = input('Put integer or float number:')
q1 = input('Is the first number an integer or float? Input "int" or "float":')
q2 = input('Is the second number an integer or float? Input "int" or "float":')
if q1 == q2 == "int":
    num1 = int(num1)
    num2 = int(num2)
elif q1 == q2 == "float":
    num1 = float(num1)
    num2 = float(num2)
elif q1 == "int" and q2 == "float":
    num1 = int(num1)
    num2 = float(num2)
elif q1 == "float" and q2=="int":
    num1 = float(num1)
    num2 = int(num2)
else:
    print("Invalid input. Please try again.")
    
operation = input('Select operation "/" "*" "+" "-" or "exit" to end program:')

while operation != "exit":

    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
        operation = input('Select operation "/" "*" "+" "-" or "exit" to end program:')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
        operation = input('Select operation "/" "*" "+" "-" or "exit" to end program:')

    elif operation == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
        operation = input('Select operation "/" "*" "+" "-" or "exit" to end program:')

    elif operation == '/':
        if num2 != 0:  # division by 0
            print(f'{num1} / {num2} = {num1 / num2}')
            operation = input('Select operation "/" "*" "+" "-" or "exit" to end program:')

        else:
            print("Error: Division by zero.")
    elif operation == 'exit':
        print("exit")
        break
