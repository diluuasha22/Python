answer1 = input("Нравится ли вам отдыхать на природе? ")
answer2 = input("Вы любите чай? ")
if answer2.lower() == "нет" and answer1.lower() == "нет":
    print("Вы мне нравитесь.")
elif answer1.lower() == "нет" and answer2.lower() == "да":
    print("Я не люблю чай.")
elif answer2.lower() == "нет" and answer1.lower() == "да":
    print("Я тоже люблю отдыхать на природе.")
elif answer1.lower() == "да" and answer2.lower() == "да":
    print("Мы с вами одного мнения.")
else:
    print("Ошибка. Укажите \"Да\" или \"Нет\".")