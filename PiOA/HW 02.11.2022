from random import *


def zapolnenie(mass1):
    mass = mass1
    n = int(input("Введите длину массива: "))
    for i in range(n): mass.append(randint(-1000, 1000))
    print("Массив заполнен случайными числами\n")
    return mass


def vivod(mass):
    print(f"Массив: \n{mass}")


def mmin(mass):
    mmin = 10 * 10 ** 15
    for i in range(len(mass)):
        if mass[i] < mmin and mass[i] > 0:
            mmin = mass[i]
    print("Минимальный элемент среди положительных", mmin, end='\n\n')


def krat7(mass):
    krat7_mass = set()
    for i in range(len(mass)):
        if abs(mass[i]) % 7 == 0:
            krat7_mass.add(mass[i])
    krat7_mass = list(krat7_mass)
    krat7_mass.reverse()
    print("Элементы кратные 7 в обратном порядке:")
    for i in krat7_mass:
        print(i, end=" ")
    print("\n")


def sorti(mass):
    for i in range(len(mass) - 1):
        m = i
        j = i + 1
    while j < len(mass):
        if mass[j] < mass[m]:
            m = j
        j = j + 1
    mass[i], mass[m] = mass[m], mass[i]
    print(f"Отсортированный массив\n{mass}")
    return mass


def vibor(mass):
    i = int(input("Введите индекс элемента, который хотите изменить: "))
    num = float(input("Введите число, на который хотите заменить выбранный элемент: "))
    mass[i] = num


def init_array():
    spisok = []
    print("Список создан!")
    return spisok


def main():
    spisok = init_array()
    while True:
        print(
            "1.Заполнить массив случайными числами\n2.Найти минимальный элемент среди положительных\n3.Вывести элементы кратные 7\n" "4.Отсортировать массив методом выбора элементов и вывести отсортированный массив на экран\n5.Редактировать нужный элемент\n" "6.Вывод массива\n0.Выход из программы")
        y = int(input("Введите цифру, под которой стоит желаемое действие: "))
        if y == 0:
            break
        if y == 1:
            spisok = zapolnenie(spisok)
        if y == 2: mmin(spisok)
        if y == 3: krat7(spisok)
        if y == 4: spisok = sorti(spisok)
        if y == 5: vibor(spisok)
        if y == 6: vivod(spisok)


main()
