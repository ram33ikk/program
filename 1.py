print("=== Подземелье ===")

hp = 100
gold = 0
level = 1
has_sword = False
inventory = []
inventory.append(["Деревянный меч", 15, 100])
poison_cost = 100
sword_cost = 300

def go_forward(hp, gold):
    
    hp = hp - 10
    gold = gold + 20
    
    print("Ты идешь вперед...")
    print("Находишь 20 золота.")
    print("Теряешь 10 здоровья.")

    return hp, gold

def open_chest(gold):
    
    gold = gold + 50
    
    print("Ты открыл сундук!")
    inventory.append(["Зелье", 30, 100])
    print("Получено: Зелье!")
    
    return gold

def battle(hp, gold, level):
    hp = hp - 25
    if has_sword:
        gold = gold + 150
        level = level + 1
        print("Получено 150 золота благодаря мечу!")
    else:
        gold = gold + 100
        level = level + 1
        print("Получено 100 золота.")
        
    print("Потеряно 25 здоровья.")
    print("Уровень повышен!")

    return hp, gold, level

def shop(poison_cost, sword_cost, hp, gold, has_sword):
    print()
    print("1 - Купить зелье (", poison_cost, ")")
    print("2 - Купить меч (", sword_cost, ")")
    print("3 - Выйти из магазина")

    shop_choice = input("Введите что хотите купить: ")

    if shop_choice == "1":
        if gold >= poison_cost:

            gold = gold - poison_cost
            hp = hp + 30

            print("Ты купил зелье здоровья!")
            print("+30 к здоровью")

            if hp > 100:
                hp = 100
        else:
            print("Не хватает золота!")

    elif shop_choice == "2":
        if gold >= sword_cost:
            has_sword = True
            gold = gold - sword_cost
        else:
            print("Недостаточно золота!")

    elif shop_choice == "3":
        return hp, gold, has_sword

    else:
        print("Не существует такого ответа!")
    
    return hp, gold, has_sword

def show_stats(hp, gold, level):

    print("===== Герой =====")
    print("Здоровье: ", hp)
    print("Золото: ", gold)
    print("Уровень", level)
    print("==================")

def show_inventory(inventory):
    print("=== Инвентарь ===")
        
    for item in inventory:
        print(item[0])
    return

def boss(level):
    if level >= 5:
        print("Ты победил босса!")
        print("Поздравляем!")
        print("Ты прошел игру!")
        return True
    else:
        print("Сначала достигни 5 уровня!")
        return False

def use_potion(hp, inventory):
    if "Зелье" in inventory:
        inventory.remove("Зелье")
        hp = hp + 30
            
        if hp > 100:
            hp = 100
    
        print("Ты использовал зелье!")
        print("Здоровье восстановлено.")
    else:
        print("У тебя нет Зелья!")
    
    return hp

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
    print("0 - Выйти из игры")

    choice = input("Выберите действие: ")

    if choice == "1":
        hp, gold = go_forward(hp, gold)

    elif choice == "2":
        gold = open_chest(gold)

    elif choice == "3":
        hp, gold, level = battle(hp, gold, level)

    elif choice == "4":
        hp, gold, has_sword = shop(sword_cost, poison_cost, hp, gold, has_sword)

    elif choice == "5":
        show_stats(hp, gold, level)

    elif choice == "6":
        show_inventory(inventory)

    elif choice == "7":
        boss_won = boss(level)
        if boss_won:
            break

    elif choice == "8":
        hp = use_potion(hp, inventory)

    elif choice == "0":
        print("Игра закрыта.")
        break

    else:
        print("Такого действия нет!")

    if hp <= 0:
        print("Ты погиб...")
        break