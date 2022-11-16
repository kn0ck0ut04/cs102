# Victor Alexandrov
# K3124, ITMO University

from math import *


def schitalka(meow: float, bark: float, command: str):
    if command == "+":
        return meow + bark
    elif command == "-":
        return meow - bark
    elif command == "/":
        if bark == 0:
            print("Деление на ноль невозможно! Попробуйте еще раз")
        else:
            return meow / bark
    elif command == "*":
        return meow * bark
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
    elif command == "log":
        if int(bark) > 0:
            if int(meow) > 0:
                return log(meow, bark)
            else:
                print('Аргумент логарифма не может быть отрицательным или равным нулю! Попробуйте заново')
        else:
            print("Основание не может быть отрицательным или равным нулю! Попробуйте заново")
    elif command == "**":
        return meow**bark
    else:
        return f"Неизвестный оператор: {command!r}."


if __name__ == "__main__":
    oper_with_odno_chislo = ["sin", "cos", "tg", "2", "ln", "lg"]
    oper_with_dva_chisla = ["+", "-", "*", "/", "**"]
    oper_log = "log"
    while True:
        COMMAND = input("Введите операцию > ")
        if COMMAND.isdigit() and int(COMMAND) == 0:
            break
        if COMMAND in oper_with_dva_chisla:
            while True:
                try:
                    MEOW = float(input("Первое число: > "))
                    BARK = float(input("Второе число: > "))
                    break
                except ValueError:
                    print("Вы ввели не число. Попробуйте еще раз")
            print(schitalka(MEOW, BARK, COMMAND))
        elif COMMAND in oper_with_odno_chislo:
            while True:
                try:
                    MEOW = float(input("Число: > "))
                    break
                except ValueError:
                    print("Вы ввели не число. Попробуйте еще раз")
            print(schitalka(MEOW, 0, COMMAND))
        elif COMMAND in oper_log:
            while True:
                try:
                    MEOW = float(input("Основание: > "))
                    BARK = float(input("Число: > "))
                    break
                except ValueError:
                    print("Вы ввели не число. Попробуйте еще раз")
            print(schitalka(BARK, MEOW, COMMAND))
        else:
            print('Неизвестная операция. Попробуйте еще раз')