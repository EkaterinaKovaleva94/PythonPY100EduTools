money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
sum1=salary+money_capital
month=0
while sum1>0:
 sum1-=spend
 spend*=1.05
 month+=1  # количество месяцев, которое можно прожить
# TODO Оформить решение

print(month)
