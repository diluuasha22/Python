total_money = int(input("Введите количество монет: "))
while (total_money // 8) > 1:
    total_money = total_money // 8
print(total_money)