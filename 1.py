# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

newList = list(map(int, input('введите числа через пробел: ').split()))
print(f'элементы на нечетных позициях {newList[1::2]}')
print(f'их сумма: {sum(newList[1::2])}')