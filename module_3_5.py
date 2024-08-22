def get_multiplied_digits(number):
    str_number = str(number)  # Преобразуем число в строку
    first = int(str_number[0])  # Получаем первую цифру в числовом представлении

    if len(str_number) > 1:  # Проверяем, если длина строки больше 1
        return first * get_multiplied_digits(
            int(str_number[1:]))  # Умножаем первую цифру на результат рекурсивного вызова
    else:
        return first  # Возвращаем первую цифру, если длина строки 1


# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24 (4 * 2 * 3)