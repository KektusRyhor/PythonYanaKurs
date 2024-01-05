# Массив из 7 цифр.
# Если четных цифр в нем больше чем нечетных,то найти сумму всех его цифр,
# если нечетных больше, то найти произведение 1 3 и 6 элемента.
mass = []
chet = []
nechet = []
result = 0
while True:
    print('Заполняем массив САМОСТОЯТЕЛЬНО!')
    i1 = int(input('Введи цифру 1:'))
    mass.append(i1)
    i2 = int(input('Введи цифру 2:'))
    mass.append(i2)
    i3 = int(input('Введи цифру 3:'))
    mass.append(i3)
    i4 = int(input('Введи цифру 4:'))
    mass.append(i4)
    i5 = int(input('Введи цифру 5:'))
    mass.append(i5)
    i6 = int(input('Введи цифру 6:'))
    mass.append(i6)
    i7 = int(input('Введи цифру 7:'))
    mass.append(i7)
    print('Основной массив: ',mass)
    for i in mass:
        if i%2 == 0:
            chet.append(i)
        else:
            nechet.append(i)
    print('Чётный массив: ', chet)
    print('Нечётный массив: ', nechet)
    if len(chet) > len(nechet):
        print(f'Сумма всех цифр массива будет равна: {i1+i2+i3+i4+i5+i6+i7}')
    else:
        print(f'Произведение {i1}, {i3}, {i6} будет равно: {i1*i2*i6}')
    break