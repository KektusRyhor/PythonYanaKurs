myDelishes = input('Блюдо от которого меня тошнит:')
delishes = ['Котлетки','Овсянка','Сосиски','Макароны','Гречка']

# Вот так я пытался это реализовать изначально
# for i in delishes:
#     print(i)
#     if i == myDelishes:
#         notFood = str('Я не ем ' + i)
#         print(notFood)
#         delishes.index(myDelishes)
#         break
for i in delishes:
    if i == myDelishes:
        print('Я не ем ' + myDelishes)
    else:
        print(i)
