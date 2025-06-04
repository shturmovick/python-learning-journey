try:
    age = int(input("Сколько тебе лет?: "))
    if age >= 60:
        print("Вы пенсионер")
    elif 18 <= age < 25:
        print("молодой взрослый")
    elif age >= 25:
        print("доступ разрешен")
    else:
        print("доступ запрещен")
except ValueError:
    print ("ошибка вводи только цифры")