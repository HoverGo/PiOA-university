## Рыженков Никита Андреевич вариант 24 (24 54 84)
import math
#24
def func(x,t):
    func = (1 + (x**2 - (2*x*t)**0.5)**0.5 ) \
           / (1 + (1+(math.sin(x))**2 + (0.3*math.cos(x*t)**2)**0.5)**0.5)
    return func
x = int(input("Введите значение x: ")); t = int(input("Введите значение t: "))
print(func(x,t))


#54
def r(a):
    radius = ( a / (3**0.5) )
    return radius
a = int(input("Введите сторону равностороннего треугольника: "))
print(r(a))


#84
number = int(input("Введите трёхзначное число: "))

def fproizv(num):
    proizv_1 = num//100 * ( (num//10)%10 )
    proizv_2 = num%10 * ( (num//10)%10 )
    return proizv_1 == proizv_2
print(fproizv(number))


## 10 с условием
def f(a,b,c,x):
    if x<3 and b!=0:
        return ( ( a*x**2 ) - ( b*x ) + c )
    elif x>3 and b==0:
        if (x-c)!=0:
            return ( ( x-a ) / ( x-c ) )
        else:
            return ("Нельзя делить на ноль")
    else:
        if c!=0:
            return ( x/c )
        else:
            return ("Нельзя делить на ноль")

a, b, c, x = map(int, (input("Введите a, b, c, x через пробел: ").split()))
print(f(a,b,c,x))