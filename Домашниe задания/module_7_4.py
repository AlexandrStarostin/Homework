#Использование %:

team1_num = 5
team2_num = 6

print('В команде Мастера кода участников: %(team1)s!' %{'team1':team1_num})

print('Итого сегодня в командах участников: %(team1)s и %(team2)s!' %{'team1':team1_num, 'team2':team2_num})

print()

#Использование format():

score_2 = 42
team1_time = 18015.2

print('Команда Волшебники данных решила задач:{scrol}!'.format(scrol=score_2))

print('Волшебники данных решили задачи за с {time}!'.format(time=team1_time))

print()


#Использование f-строк:

score_1 = 42
score_2 = 42

team1_time = 22
team2_time = 22888

print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастера кода!')

elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print('Победа команды Волшебники Данных!')

else:
    print('Ничья!')


tasks_total = score_1 + score_2
time_avg = (score_1+score_2)/(team1_time+team2_time)

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

