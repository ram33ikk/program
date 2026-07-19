hp = 100
gold = 50
damage = 10
enemy_hp = 30

def character_info():
    print("Твои характеристики:")
    print("HP: ", hp)
    print("Золото: ", gold)
    print("Урон: ", damage)

def attack_dummy(enemy_hp, damage):
    print("Вы атакуете манекен!")
    enemy_hp = enemy_hp - damage
    print("Нанесено", damage, "урона.")
    if enemy_hp > 0:
            print("У манекена осталось", enemy_hp, "HP.")
    else:
            print("Манекен уничтожен!")
            enemy_hp = 30
    return
print("===FirstRPG===")

name_hero = input("Введите имя героя: ")

print("Добро пожаловать,", name_hero, "!")

while True:
    print("===FirstRPG===")
    print()
    print("1 - Показать характеристики")
    print("2 - Тренировочный манекен")
    print("0 - Выйти из игры")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        character_info()
    
    elif choice == "2":
        attack_dummy(enemy_hp, damage)
        
    elif choice == "0":
        print("До скорой встречи!")
        break

    else:
        print("Не такого пункта меню!")