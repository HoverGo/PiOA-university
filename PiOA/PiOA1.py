## 1
# def f1(a,b,c,x):
#     if x<0 and b!=0:
#         if (c*x - a):
#             return ("Ошибка, нельзя делить на ноль. ветка 1")
#         else:
#             return (2*x-b) / (c*x - a)
#     elif x>0 and b==0:
#         if x-7==0:
#             return ("Ошибка, нельзя делить на ноль. ветка 2")
#         else:
#             return (x-a) / (x-7)
#     else:
#         if c == 0 or 2-x == 0:
#             return ("Ошибка, нельзя делить на ноль. ветка 3")
#         else:
#             return ((4-x) / c) + ((-c) / (2-x))
# a1, b1, c1, x1 = map(int, (input("Введите a, b, c, x через пробел: ").split()))
# print(f1(a1,b1,c1,x1))


## 2
x2 = int(input("Введите координату x: "))
y2 = int(input("Введите координату y: "))

def f2(x,y):
    if (x**2+y**2 - 225 == 0 or (x==y and x+y<=20)):
        return "Точка на границе графика"
    if (x**2+y**2 - 225) < 0 and y>abs(x):
        return "Точка внутри графика"
    if (x**2+y**2 - 225) > 0 or y<abs(x):
        return "Точка за графиком"
print(f2(x2,y2))

