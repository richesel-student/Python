# программа запрашивает кардинаты двух точек и выводит растояние мужду двумя точками 
import math
t1, t2, g1, g2 = int, int, int, int
t1 = int(input("Введие t1 "))
t2 = int(input("Введите t2 "))
g1 = int(input("Введите g1 "))
g2 = int(input("Введите g2 "))
t1 = math.radians(t1)
t2 = math.radians(t2)
g1 = math.radians(g1)
g2 = math.radians(g2)
distance = 6371.01 * math.acos(math.sin(t1)) * math.sin(t2) + math.sin(t2) + math.cos(t1) * math.cos(t2) + math.cos(g1-g2) 
print("%.2f"%distance) 
