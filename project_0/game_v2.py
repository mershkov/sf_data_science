"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
        Функция принимает загаданное число и возвращает число попыток
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    
    return count


def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
        Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)  # Начальное приближение

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number: int = 1) -> int:
    """Метод бисекции - на каждом шаге предположением является середина отрезка,
    границы двигаются в зависимости больше или меньше середина отрезка чем загаданное число
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    # Ваш код начинается здесь
    count = 0
    # Наименьшее и наибольшее значения случайных чисел
    a=1
    b=100
    # Предполагаемое число - середина отрезка 
    predict = round((a+b)/2)
    
    # обработка пограничных значений
    if number == 1 or number==100:
        return 1
    # увеличиваем счетчик попыток на 2 так сделали две попытки(проверили 1 и 100)
    count += 2
    
    while number != predict:
        count += 1
        if number > predict:
            a=predict
        elif number < predict:
            b=predict
        predict = round((a+b)/2)
    # Ваш код заканчивается здесь

    return count




def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
    #random_array = list(range(1,101))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score



if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(game_core_v2)
    score_game(game_core_v3)
