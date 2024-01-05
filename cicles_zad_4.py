# Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.

arr = [5,48,42,6,5,58,2,5,4,48,9,1,4,48]
arr_null = []

for i in arr:
    if arr.count(i)>2:
        arr_null.append(i)

print(arr_null)