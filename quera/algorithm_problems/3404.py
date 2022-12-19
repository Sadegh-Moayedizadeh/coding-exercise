def calculate_bmi(weight: float, height: float) -> float:
    return weight / height**2


if __name__ == '__main__':
    weight = int(input())
    height = float(input())
    bmi = calculate_bmi(weight, height)
    string = str(round(bmi, 2))
    if string[-2] == '.':
        string += '0'
    print(string)
    if bmi < 18.5:
        print('Underweight')
    elif 18.5 <= bmi < 25:
        print('Normal')
    elif 25 <= bmi < 30:
        print('Overweight')
    else:
        print('Obese')
