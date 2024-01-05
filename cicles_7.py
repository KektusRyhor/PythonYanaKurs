symbol = input('Введите символ для границы прямоугольника: ')
separ = input("Введите желаемый разделитель: ")
width = int(input("Введите желаемую ширину прямоугольника: "))
height = int(input("Введите желаемую высоту прямоугольника: "))

for i in range(height):
    if i == 0 or i == height - 1:
        print(symbol * width)
    else:
        print(f'{symbol}{separ*(width-2)}{symbol}')