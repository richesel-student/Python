# Программа запрашивает количество грамм безделушек и сувениров
suvenir = int(input("ввевди сколько сувеноров "))
bezdeluchka = int(input('введи сколько приобетено бездилушок '))
s_sum, sum_b = int, int
s_sum = (suvenir * 75) + (bezdeluchka * 125)
print("Общий вес посылки %d грамм" % (s_sum))
