# арифмитические операции
import math
a = int(input("Ввведите первое число "))
b = int(input("Введите второе число " ))
def sum(a, b):
    total = a + b
    print("Cумма a+b=%.2f"% total)



    
def minus(a, b):
    print("Разность a-b = %d" % (a - b)) 


def quotient_of_division(a, b):
    print("Частное от деление a на b = %.2f" % (a % b))

def integer_division(a, b):
    print("Целочисленное деление %.2f" % (a/b))

print("Логарифм двух чисел %.2f" % math.log(a))
print("Степень числа %.2f" % (a**b))


sum(a,b)
minus(a,b)
quotient_of_division(a, b)
integer_division(a, b)
