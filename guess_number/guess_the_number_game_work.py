import numpy as np

count = 0  # счетчик попыток
number = np.random.randint(1, 101)  # загадали число
print("Загадано число от 1 до 100")

def game_core_v2(number):
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 10
        elif number < predict:
            predict -= 10
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 10
    return(count) # выход из цикла, если угадали

count = (game_core_v2(number))
print(f"Вы угадали число {number} за {count} попыток.")

def score_game(game_core_v2):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)