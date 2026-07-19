print("=== Подземелье ===")

hp = 100
gold = 0

while True:

    print()
    print("1 - Идти вперед")
    print("2 - Открыть сундук")
    print("3 - Сражаться")
    print("4 - Магазин")
    print("5 - Показать характеристики")
    print("6 - Инвентарь")
    print("0 - Выйти из игры")

    choice = input("Выберите действие: ")

    if choice == "1":
        hp = hp - 10
        gold = gold + 20

        print("Ты идешь вперед...")
        print("Находишь 20 золота.")
        print("Теряешь 10 здоровья.")
    elif choice == "2":
        for chest in range(1,4):
            print("Открывается сундук", chest)
        print("Все сундуки открыты!")
        
        gold = gold + 50
        print("Ты получил 50 золота!")

    elif choice == "3":
        for battle in range(1,4):
            print("Раунд", battle)
        print("Победа!")

        hp = hp - 25
        gold = gold + 100

        print("Получено 100 золота.")
        print("Потеряно 25 здоровья")

    elif choice == "4":

        if gold >= 100:
            gold = gold - 100
            hp = hp + 30

            if hp > 100:
                hp = 100

            print("Ты купил зелье!")
            print("+30 здоровья")

        else:
            print("Недостаточно золота.")
    
    elif choice == "5":

        print("===== Герой =====")
        print("Здоровье: ", hp)
        print("Золото: ", gold)
        print("==================")

    elif choice == "6":
        print("=== Инвентарь ===")
        print("Меч")

    elif choice == "0":
        print("Игра закрыта.")
        break

    else:
        print("Такого действия нет!")

    if hp <= 0:
        print("Ты погиб...")
        break