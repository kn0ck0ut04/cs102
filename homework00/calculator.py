from math import *


def schitalka(meow: float, bark: float, command: str):
    if command == "+":
        return meow + bark
    elif command == "-":
        return meow - bark
    elif command == "/":
        return meow / bark
    elif command == "*":
        return meow * bark
    elif command == "":
        return meow, bark
    elif command == "2":
        return meow**2
    elif command == "sin":
        return sin(meow)
    elif command == "cos":
        return cos(meow)
    elif command == "tg":
        return tan(meow)
    elif command == "ln":
        return log(meow)
    elif command == "lg":
        return log(meow, 10)
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    match_case_calc_one = ["sin", "cos", "tg", "2", "ln", "lg"]
    match_case_calc_two = "+-*/**log"
    while True:
        COMMAND = input("Введите операцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND in match_case_calc_two:
            MEOW = float(input("Первое число > "))
            BARK = float(input("Второе число > "))
            print(schitalka(MEOW, BARK, COMMAND))
        elif COMMAND in match_case_calc_one:
            MEOW = float(input("Число > "))
            print(schitalka(MEOW, 0, COMMAND))
