# Home work 5.1 -- A leap year.
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

test_data = [1500, 1900, 2000, 2016, 1987]
test_results = [False, False, True, True, False]

for year, result in zip(test_data,test_results):
    if is_year_leap(year) == result:
        print(year, 'is leap? -->', result)
    else:
        print(year, 'from your func -->', is_year_leap(year))
        print('but expected -->', result)


# Lab 5.3 -- Factorial.
def factorial(num):
    if num < 0:
        return None
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Vvedite chislo dlya kotorogo nuzhno poschitat' faktorial:"))
factorial_num = factorial(num)
print("Faktorial chisla", num, "=", factorial_num)

# Home work 5.4 -- Fibonacci numbers.
"""Function for Fibonacci numbers and output its in range(-1,25)"""
def febo(n):
    if n<1:
        return None
    if n<3:
        return 1
    return febo(n-1)+febo(n-2)

print('Fibonacci numbers in range(-1,25):')

for n in range(-1,25):
    print(febo(n))
