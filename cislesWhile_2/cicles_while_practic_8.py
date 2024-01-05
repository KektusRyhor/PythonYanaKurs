# Казино. Компьютер генерирует числа от 1 до 10 и от 1 до 2-х соответственно.
# Цифры от одного до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный,2 черный).
# Пользователю дается 5 попыток угадать номер и цвет(Прим. введения с клавиатуры: 3 красный).
# В случае неудачи вывести на экран правильную комбинацию.
import random
massChisla = random.randint(1,2)
massCvet = random.randint(1,2)
count = 2
while count != 0:
    tryChisla = int(input('Введи число от 1 до 10: '))
    if tryChisla == massChisla:
        print(f'Ты угадал число: {tryChisla}')
    else:
        print('Ты не угадал число, пробуй ещё!')

    tryCvet = int(input('Введи цвет (1-красный,2 черный): '))
    if tryCvet == massCvet:
        print(f'Ты угадал цвет: {tryCvet}')
    else:
        print('Ты не угадал цвет, пробуй ещё!')
    if tryChisla == massChisla and tryCvet == massCvet:
        print('Ты всё угадал')
        break
    elif tryChisla == massChisla and tryCvet != massCvet:
        print(f'Ты угадал число {massChisla}, но не угадал цвет {massCvet}')
    elif tryCvet == massCvet and tryChisla != massChisla:
        print(f'Ты угадал цвет {massCvet}, но не угадал цифру {massChisla}')
    count -=1
    print(f'Осталось {count} попыток')
