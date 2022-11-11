from random import *


# 23.Дан  двумерный  массив  размером N*M.
# Определить,  есть  ли  в  данном  массиве строка,
# содержащая больше положительных элементов, чем отрицательных.

def init_array():
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    spisok = [[randint(-50, 25) for i in range(m)] for j in range(n)]
    print("Список создан!")
    print(spisok)
    return spisok


def print_1(mass):
    print("Список:")
    print(mass)


def vibor(mass):
    i = int(input("Введите индекс строки для изменения элемента: "))
    j = int(input("Введите индекс столбца для изменения элемента: "))
    mass[i][j] = float(input("Введите элемент, на который хотите заменить: "))
    return mass


def counting(mass):
    buly = False
    for i in range(len(mass)):
        minus = 0
        plus = 0
        for j in range(len(mass[0])):
            if mass[i][j] < 0:
                minus += 1
            elif mass[i][j] > 0:
                plus += 1
        if plus > minus:
            buly = True
            break
    if buly:
        print("В списке имеется строка, содержащая больше положительных элементов, чем отрицательных.")
    else:
        print("В списке нет строки, содержащей больше положительных элементов, чем отрицательных")


def main():
    spisok = init_array()
    vibor(spisok)
    print_1(spisok)
    counting(spisok)


main()
