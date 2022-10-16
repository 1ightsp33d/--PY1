money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
def lifelength(cap, sal, sp, inc):
    i=0
    while cap > 0:
        cap -= sp * ( 1 + inc ) ** i
        if cap < 0:
            break
        cap += sal
        i += 1
    return i
# TODO Оформить решение
month=lifelength(money_capital,salary,spend,increase)
print(month)
