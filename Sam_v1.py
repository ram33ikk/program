hero = {
    "hp": 100,
    "mana": 0,
    "level": 1,
    "gold": 0,
    "damage": 5,   
}
dummy = {
    "hp": 100
}
rat = {
    "hp": 20,
    "level": 1,
    "damage": 5,
    "loot": 2
}
hog = {
    "hp": 50,
    "level": 3,
    "damage": 10,
    "loot": 4
}
bear = {
    "hp": 100,
    "level": 8,
    "damage": 15,
    "loot": 7
}
skeleton = {
    "hp": 150,
    "level": 15,
    "damage": 20,
    "loot": 10
}
goblin = {
    "hp": 250,
    "level": 25,
    "damage": 35,
    "loot": 20
}

while True:
    print("=" * 40)
    print("              SAM v1.0")
    print("=" * 40)
    print("1 - Новая игра")
    print("2 - Загрузить игру")
    print("3 - Настройки")
    print("0 - Выход из игры")
    print("=" * 40)

    choice_menu = input("Выберите пункт: ")