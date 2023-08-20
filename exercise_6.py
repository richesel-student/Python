# Программа расчитывает чаевые,ндс, b и сумму заказа 
order_sum = float(input("Какова сумма заказа в ресторане "))
nds, tea_sum, = float, float
nds =  (order_sum * 18.0) / 100.0 # налог на сумму заказа 18%
tea_sum = (order_sum * 18.00) / 100.00 # cумма за оплату чаевх
over_sum =  order_sum + nds + tea_sum
print('Cумма налога равна  %.2f\nCумма чаевых равана %.2f\nИтого с ндс + заказov + чаевые %.2f '% (nds, tea_sum, over_sum))
