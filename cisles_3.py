# Задача №1: Лотерея
# Реализуйте свою игру лотереи с выбором числа или набора чисел
import random

youStep = str(input('Введи своё число от 0 до 100:'))
compStep = str(random.randint(0,5))
choiseCount = 10
n = ''
for i in n:
    if int(youStep) < int(compStep):
        print('Твоё число меньше, пробуй ещё')
    elif int(youStep) > int(compStep):
        print("Твоё число больше, пробуй ещё")
    elif int(youStep) == int(compStep):
        break
        print('ты победил')
    else:

        print('Ты проиграл')


