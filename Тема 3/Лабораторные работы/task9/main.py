salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 1.03  # рост цен
need_money = 0
for i in range(months):
    diff = spend-salary
    need_money += diff
    spend *= increase
#need_money=0 # количество денег, чтобы прожить 10 месяцев
# TODO Оформить решение
print(round(need_money))
