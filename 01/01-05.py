line1 = input("Первая строка: ")
line2 = input("Вторая строка: ")
line3 = input("Третья строка: ")
if ((line1 == "раз" or line1 == "один") and line2 == "два" and line3 == "три") or\
 (line1 == "1" and line2 == "2" and line3 == "3"):
    print("Гори")
else:
    print("Не гори")