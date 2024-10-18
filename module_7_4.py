"""
Дегтярев Виталий (группа 22/08)
Домашнее задание №7.4
Домашнее задание по теме "Форматирование строк".
"""

# Запуск
if __name__ == '__main__':
    # Исходные данные
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451

    # Вычисляемые значения
    tasks_total = None
    time_avg = None
    challenge_result = None

    # Использование %:
    print('В команде Мастера кода участников: %s' % team1_num)
    print('В команде Волшебники данных участников: %s' % team2_num)
    print('Итого сегодня в командах участников: %s и %s\n' % (team1_num, team2_num))

    # Использование format():
    print('Команда Мастера кода решила задач: {} !'.format(score_1))
    print('Команда Волшебники данных решила задач: {} !\n'.format(score_2))
    print('Мастера кода решили задачи за {}с!'.format(team1_time))
    print('Волшебники данных решили задачи за {}с!\n'.format(team2_time))

    # Использование f-строк:
    print(f'Команды решили {score_1} и {score_2} задач.\n')

    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победа команды Волшебники Данных!'
    else:
        challenge_result = 'Ничья!'
    print(f'Результат битвы: {challenge_result}\n')

    tasks_total = score_1 + score_2
    time_avg = round((team1_time + team2_time)/tasks_total, 1)
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

