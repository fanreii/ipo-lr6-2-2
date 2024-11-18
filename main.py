import random as rn # модуль random для генерации случайных чисел
sum = 0 # переменная для дальнейшего подсчета суммы
height = rn.randint(4,8) # рандомное число из диапазона
width = rn.randint(4,8) # рандомное число из диапазона
list = [-15, -4, -2, -7, 0, 3, 5, 12, 7] # список значений для заполнения матрицы
matrix = [] # создание матрицы 
for i in range(height): # цикл for 
    row = [] # создание рядов для матрицы
    for o in range(width): # цикл for 
        row.append(rn.choice(list)) # заполнение рядов числами из диапазона list
    matrix.append(row) # заполнение матрицы созданными рядами
for row in matrix: # цикл for для рядов 
    for num in row: # для каждого числа в ряду 
        print(num, end = ' ') # вывод чисел в рядах через пробел
    print() # вывод рядов
for row in matrix: # цикл for 
    for numbers in row: # для чисел в рядах 
        if numbers % 2 != 0: # если число не кратно 2
            sum += numbers # складываем это число
print("Сумма нечетных значений: ",numbers) # вывод