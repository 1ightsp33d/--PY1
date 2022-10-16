salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def needed(sal, sp, m, inc):
    need_money=abs(sal-sp)
    for i in range(1,m):
        need_money+=sp*(1+inc)**i-sal
    return need_money

need_money=needed(salary,spend,months,increase)

print(round(need_money))
