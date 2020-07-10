day_list = ['1. Понедельник', '2. Вторник', '3. Среда', '4. Четверг', '5. Пятница', '6. Суббота', '7. Воскресенье']

for i in day_list:
    print(i)

select_day = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье',
}

while True:
    number_day = int(input('Введите номер: '))
    if number_day <= 7 :
        print(select_day.get(number_day))
    else:
        print('Введите число от 1 до 7!')
        continue
    