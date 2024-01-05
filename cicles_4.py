text = input('Введи предложение:')
letter = input('Введи букву для удаления:')

for i in text:
    if i == letter:
        continue
    print(i)


# Посмотрел решение, вижу, что можно сделать лучше и по другому