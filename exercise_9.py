# Программа запрашивает сумму начального депазита,  на  3  года   под ставку 4 % ставку.
one_year = float(input("сколько денег в начале первого года "))
percent_one_year = (one_year * 1.04) # 4 % процента от 100%-1.04
two_year_percent = percent_one_year * 1.04
three_year_percent = two_year_percent * 1.04
print("За первый год вы заработаете %.2f рублей \n За втрой год заработаете %.2f рублей \n За третий год вы заработаете %.2f рублей " % (percent_one_year, two_year_percent, three_year_percent))
