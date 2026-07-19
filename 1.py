import ast

class Player:
    pass

print("=== Подземелье ===")

player = {
    "hp": 100,
    "gold": 0,
    "level": 1,
    "has_sword": False,
    "inventory": [["Деревянный меч", 15, 100]]
}
poison_cost = 100
sword_cost = 300

def go_forward(player):
    
    player["hp"] -= 10
    player["gold"] += 20
    
    print("Ты идешь вперед...")
    print("Находишь 20 золота.")
    print("Теряешь 10 здоровья.")

    return

def open_chest(player):
    
    player["gold"] +=50
    
    print("Ты открыл сундук!")
    player["inventory"].append(["Зелье", 30, 100])
    print("Получено: Зелье!")
    
    return

def battle(player):
    player["hp"] -=25
    if player["has_sword"]:
        player["gold"] += 150
        player["level"] += 1
        print("Получено 150 золота благодаря мечу!")
    else:
        player["gold"] += 100
        player["level"] += 1
        print("Получено 100 золота.")
        
    print("Потеряно 25 здоровья.")
    print("Уровень повышен!")

    return

def shop(poison_cost, sword_cost, player):
    print()
    print("1 - Купить зелье (", poison_cost, ")")
    print("2 - Купить меч (", sword_cost, ")")
    print("3 - Выйти из магазина")

    shop_choice = input("Введите что хотите купить: ")

    if shop_choice == "1":
        if player["gold"] >= poison_cost:

            player["gold"] -= poison_cost
            player["hp"] += 30

            print("Ты купил зелье здоровья!")
            print("+30 к здоровью")

            if player["hp"] > 100:
                player["hp"] = 100
        else:
            print("Не хватает золота!")

    elif shop_choice == "2":
        if player["gold"] >= sword_cost:
            player["has_sword"] = True
            player["gold"] -= sword_cost
        else:
            print("Недостаточно золота!")

    elif shop_choice == "3":
        return

    else:
        print("Не существует такого ответа!")
    
    return

def show_stats(player):

    print("===== Герой =====")
    print("Здоровье: ", player["hp"])
    print("Золото: ", player["gold"])
    print("Уровень", player["level"])
    print("==================")

def show_inventory(player):
    print("=== Инвентарь ===")
        
    for item in player["inventory"]:
        print(item[0])
    return

def boss(player):
    if player["level"] >= 5:
        print("Ты победил босса!")
        print("Поздравляем!")
        print("Ты прошел игру!")
        return True
    else:
        print("Сначала достигни 5 уровня!")
        return False

def use_potion(player):
    if ["Зелье", 30, 100] in player["inventory"]:
        player["inventory"].remove(["Зелье", 30, 100])
        player["hp"] += 30
            
        if player["hp"] > 100:
            player["hp"] = 100
    
        print("Ты использовал зелье!")
        print("Здоровье восстановлено.")
    else:
        print("У тебя нет Зелья!")
    
    return

while True:

    print()
    print("1 - Идти вперед")
    print("2 - Открыть сундук")
    print("3 - Сражаться")
    print("4 - Магазин")
    print("5 - Показать характеристики")
    print("6 - Инвентарь")
    print("7 - Босс")
    print("8 - Использовать зелье")
    print("9 - Сохранить игру")
    print("10 - Загрузить последнее сохранение")
    print("0 - Выйти из игры")

    choice = input("Выберите действие: ")

    if choice == "1":
        go_forward(player)

    elif choice == "2":
        open_chest(player)

    elif choice == "3":
        battle(player)

    elif choice == "4":
        shop(poison_cost, sword_cost, player)

    elif choice == "5":
        show_stats(player)

    elif choice == "6":
        show_inventory(player)

    elif choice == "7":
        boss_won = boss(player)
        if boss_won:
            break

    elif choice == "8":
        use_potion(player)

    elif choice == "9":
        file = open("save.txt", "w")
        file.write(str(player["hp"]))
        file.write("\n")
        file.write(str(player["gold"]))
        file.write("\n")
        file.write(str(player["level"]))
        file.write("\n")
        file.write(str(player["has_sword"]))
        file.write("\n")
        file.write(str(player["inventory"]))
        file.close()
        print("Игра сохранена.")

    elif choice == "10":
            try:
                file = open("save.txt", "r")
                text = file.read()
                lines = text.split("\n")
                player["hp"] = int(lines[0])
                player["gold"] = int(lines[1])
                player["level"] = int(lines[2])
                if lines[3] == "True":
                    player["has_sword"] = True
                else:
                    player["has_sword"] = False
                player["inventory"] = ast.literal_eval(lines[4])
                file.close()
                print("Файл сохранения загружен.")
            except:
                print("Файла сохранения нет!")
        

    elif choice == "0":
        print("Игра закрыта.")
        break

    else:
        print("Такого действия нет!")

    if player["hp"] <= 0:
        print("Ты погиб...")
        break