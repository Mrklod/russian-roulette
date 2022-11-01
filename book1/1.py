import random
def game():
    """Блэкджек
    чтобы взять карту нажмите enter,чтобы не брать введите stop"""
    game_win = 21
    point = 0
    vrag = random.randint(10,21)
    while point <21:
        c = random.randint(6, 13)
        b = input("Берёте карту?: ")
        if b == "stop":
            break
        point = point + c
        if point > 21:
            return "Вы проиграли,перебор"
        print(point)
    if point>vrag:
        return f"У Вас {point} очков,у противника {vrag},Вы победили"
    if point<vrag:
        return f"У Вас {point} очков,у противника {vrag},Вы проиграли "
print(game())
