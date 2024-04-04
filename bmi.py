def calculate_bmi(weight, height):
    """
    Function to calculate BMI (Body Mass Index)
    :param weight: weight in kilograms (float)
    :param height: height in meters (float)
    :return: BMI value (float)
    """
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    """
    Function to classify BMI into categories
    :param bmi: BMI value (float)
    :return: BMI category (string)
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    print("Please enter your weight (in kilograms):")
    weight = float(input())
    print("Please enter your height (in meters):")
    height = float(input())

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")


if __name__ == "__main__":

    main()
    
    
    
    