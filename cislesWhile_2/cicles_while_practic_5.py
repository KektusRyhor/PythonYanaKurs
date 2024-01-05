# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

# first = float(input('Первое число: '))
# second = float(input('Второе число: '))
# operation = input('Введи действие(+ - * / 0): ') !!!! до меня не дошло, почему переменные нужно включать в цикл

while True:
    first = float(input('Первое число: '))
    second = float(input('Второе число: '))
    operation = input('Введи действие(+ - * / 0): ')
    if operation == '+':
        print(f' {first} + {second} = {first+second}')
        # break
    elif operation == '-':
        print(f' {first} - {second} = {first-second}')
        # break
    elif operation == '*':
        print(f' {first} * {second} = {first*second}')
        # break
    elif operation == '/':
        if second != 0:
            print(f' {first} / {second} = {first/second}')
        else:
            print('Деление на ноль!')
        # break
    elif operation == '0':
        print('ЗАКОНЧИЛИ!')
        break
# else:
#     print('Деление на ноль!')