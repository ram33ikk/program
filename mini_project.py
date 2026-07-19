salary = int(input("Введите заработную плату:"))
debt = int(input("Введите обязательный платеж по Сплиту:"))
food_cost = int(input("Введите расходы на еду:"))

ostatok = salary - (debt + food_cost)
ostatok_mashina = ostatok - 30000
print("Свободных денег осталось:", ostatok)
print("Свободных денег не считая непредвиденные расходы:", ostatok_mashina)

if ostatok_mashina > 0:
    print("Можно отложить деньги на машину.")
else:
    print("Пока лучше направить свободные деньги на закрытие долга.")