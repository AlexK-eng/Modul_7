# Исходные данные для формирования строк


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


# Использование %:
# Количество участников первой команды (team1_num)
# Количество участников в обеих командах (team1_num, team2_num)


print('В команде  %s' % 'Мастера кода участников:', team1_num, '!')
print('Итого сегодня в командах участников %s' % team1_num, 'и', team2_num,'!')


# Использование format():
# Количество задач решённых командой 2 (score_2)
# Время за которое команда 2 решила задачи (team1_time)


print('Команда {} данных решила задач: {} !'.format('Волшебники', score_2))
print('Волшебники данных решили задачи за {time} c !'.format(time = team2_time))


# Использование f-строк:


print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = challenge_result
else:
    result = 'Ничья!'
print('Результат битвы:', result)

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')