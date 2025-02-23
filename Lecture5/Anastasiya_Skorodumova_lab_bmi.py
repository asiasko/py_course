# BMI Summary ИМТ.
"""BMI measurement software"""

def BMI(weight,height):  # BMI determination function. 
    if weight < 20 or height < 50:  # Baby check.
        print("Incorrect values. Try again.")
    return weight / (height / 100)**2


def analize_BMI(result):
# Function for analizes results of BMI.
# Data from - https://www.calculator.net/bmi-calculator.html.
    if result < 16:
        return 'Severe thinness'
    if result < 17 and result > 16:
        return 'Moderate thinness'
    if result < 25 and result > 18.5:
        return 'Normal'
    if result < 30 and result > 25:
        return 'overweight'
    if result < 35 and result > 30:
        return 'Obese Class I'
    if result < 40 and result > 35:
        return 'Obese Class II'
    if result > 40:
        return 'Obese Class III'

def main_menu():
    print(' -----------------------------------------------')
    print('|                                               |')
    print('|                                               |')
    print('|          Welcome to the AWESOME BMI!          |')
    print('|                                               |')
    print('|                                               |')
    print(' -----------------------------------------------')
    print("Welcome to the AWESOME BMI!")
    print("1. Enter your weight in kg and your height in cm")
    print("2. Your BMI")
    print("3. Result of BMI")
    print("4. Exit")

    while True:
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            weight = float(input('Enter your weight in kg:'))
            height = float(input('Enter your height in cm:'))
            print(f'Your weight = {weight}, your height = {height}')
        elif choice == "2":
            value = BMI(weight, height)
            print('Your BMI value = ',value)
        elif choice == "3":
            result = analize_BMI(value)
            print('Your BMI value = ',result)
        elif choice == "4":
            print("...Exit...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
