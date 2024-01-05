# Пользователь вводит два числа c клавиатуры,
# необходимо вывести на экран все отрицательные числа, лежащие между ними.
# Например пользователь ввел -5 и 3, на экране вывелось -4, -3, -2, -1

# print('Выведутся отрицательные числа между 1-м и 2-м числом, которые ты введёшь.')
# first = int(input('Введи первое число:'))
# second = int(input('Введи второе число:'))
# mass = range(first,second)
# mass2 = []
# i = first
# while True:
#     if i >= second:
#         if i < 0:
#             mass2.append(i)
#     i -= 1
#     if i < second:
#         break
# print(mass2)
print('Выведутся отрицательные числа между 1-м и 2-м числом, которые ты введёшь.')
first = int(input('Введи первое число:'))
second = int(input('Введи второе число:'))
while first < second:
    first += 1
    if first == 0:
        break
    print(first)