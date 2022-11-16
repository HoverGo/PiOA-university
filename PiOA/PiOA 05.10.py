from random import *


def init_array():
    spisok = []
    print("Список создан!")
    return spisok


def zapolnenie(mass1):
    mass = mass1
    n = int(input("Введите длину массива: "))
    for i in range(n):
        mass.append(randint(-10, 10))
    print("Массив заполнен случайными числами\n")
    print(mass)
    return mass


def nomera(mass):
    bolshe = []
    ravni = []
    menshe = []
    k = float(
        input("Введите число, для которого нужно найти номера элементов в списке, которые больше, меньше и равны: "))
    for i in range(len(mass)):
        if k < mass[i]:
            bolshe.append(i)
        elif k > mass[i]:
            menshe.append(i)
        else:
            ravni.append(i)
    print("Номера элементов, которые больше k: ", end=" ")
    for i in bolshe:
        print(i, end=" ")
    print("\nНомера элементов, которые равны k: ", end=" ")
    for i in ravni:
        print(i, end=" ")
    print("\nНомера элементов, которые меньше k: ", end=" ")
    for i in menshe:
        print(i, end=" ")


A = init_array()
A = zapolnenie(A)
nomera(A)
