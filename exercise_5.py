# Программа запрашивает количество бутылок литроых и больше 
bootls_1 = int(input("Какое количесво бутылок сдано литровых или меньше литра "))
bootls_2 = int(input("Какое количество бутылок сдано объемом более литра "))
litr, min_litr, sum_lirt, sum_min_litr, total = float, float, float, float, float
litr = 0.25 # Цена за одну бутылку размере больше литра 
min_litr = 0.10 # Цена за одну бутылку литр и меньше 
bootls_1 = float(bootls_1)
bootls_2 = float(bootls_2)
sum_lirt = litr * bootls_2 # сумма бутылок более литра
sum_min_litr = min_litr * bootls_1 # сумма бутылок менее литра
total = sum_lirt + sum_min_litr
print("Цена за сдачу всех бутылок %.2f $" % total)



