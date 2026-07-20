import ast

class Player:
    def __init__(self):
        self.hp = 100
        self.gold = 0
        self.level = 1
        self.has_sword = False
        self.inventory = [["Деревянный меч", 15, 100]]

    def go_forward(self):

        self.hp -= 10
        self.gold += 20
        
        print("Ты идешь вперед...")
        print("Находишь 20 золота.")
        print("Теряешь 10 здоровья.")

        return
    
    def open_chest(self):
        
        self.gold +=50
        
        print("Ты открыл сундук!")
        self.inventory.append(["Зелье", 30, 100])
        print("Получено: Зелье!")
        
        return
    def battle(self):
        self.hp -=25
        if self.has_sword:
            self.gold += 150
            self.level += 1
            print("Получено 150 золота благодаря мечу!")
        else:
            self.gold += 100
            self.level += 1
            print("Получено 100 золота.")
            
        print("Потеряно 25 здоровья.")
        print("Уровень повышен!")

        return

    def shop(self, poison_cost, sword_cost):
        print()
        print("1 - Купить зелье (", poison_cost, ")")
        print("2 - Купить меч (", sword_cost, ")")
        print("3 - Выйти из магазина")

        shop_choice = input("Введите что хотите купить: ")

        if shop_choice == "1":
            if self.gold >= poison_cost:

                self.gold -= poison_cost
                self.hp += 30

                print("Ты купил зелье здоровья!")
                print("+30 к здоровью")

                if self.hp > 100:
                    self.hp = 100
            else:
                print("Не хватает золота!")

        elif shop_choice == "2":
            if self.gold >= sword_cost:
                self.has_sword = True
                self.gold -= sword_cost
            else:
                print("Недостаточно золота!")

        elif shop_choice == "3":
            return

        else:
            print("Не существует такого ответа!")
        
        return

    def show_stats(self):
        print("===Твои характеристики===")
        print()
        print("Здоровье:", self.hp)
        print("Золото:", self.gold)
        print("Твой уровень:", self.level)
        return

    def show_inventory(self):
        print("=== Инвентарь ===")
            
        for item in self.inventory:
            print(item[0])
        return

    def boss(self):
        if self.level >= 5:
            print("Ты победил босса!")
            print("Поздравляем!")
            print("Ты прошел игру!")
            return True
        else:
            print("Сначала достигни 5 уровня!")
            return False

    def use_potion(self):
        if ["Зелье", 30, 100] in self.inventory:
            self.inventory.remove(["Зелье", 30, 100])
            self.hp += 30
                
            if self.hp > 100:
                self.hp = 100
        
            print("Ты использовал зелье!")
            print("Здоровье восстановлено.")
        else:
            print("У тебя нет Зелья!")
        
        return
    
    def save_game(self):
        file = open("save.txt", "w")
        file.write(str(player.hp))
        file.write("\n")
        file.write(str(player.gold))
        file.write("\n")
        file.write(str(player.level))
        file.write("\n")
        file.write(str(player.has_sword))
        file.write("\n")
        file.write(str(player.inventory))
        file.close()
        print("Игра сохранена.")
    
    def load_game(self):
        try:
            file = open("save.txt", "r")
            text = file.read()
            lines = text.split("\n")
            player.hp = int(lines[0])
            player.gold = int(lines[1])
            player.level = int(lines[2])
            if lines[3] == "True":
                player.has_sword = True
            else:
                player.has_sword = False
            player.inventory = ast.literal_eval(lines[4])
            file.close()
            print("Файл сохранения загружен.")
        except:
            print("Файла сохранения нет!")

print("=== Подземелье ===")

player = Player()

poison_cost = 100
sword_cost = 300



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
        player.go_forward

    elif choice == "2":
        player.open_chest

    elif choice == "3":
        player.battle

    elif choice == "4":
        player.shop

    elif choice == "5":
        player.show_stats

    elif choice == "6":
        player.show_inventory

    elif choice == "7":
        boss_won = player.boss
        if boss_won:
            break

    elif choice == "8":
        player.use_potion

    elif choice == "9":
        player.save_game

    elif choice == "10":
        player.load_game
        
    elif choice == "0":
        print("Игра закрыта.")
        break

    else:
        print("Такого действия нет!")

    if player.hp <= 0:
        print("Ты погиб...")
        break