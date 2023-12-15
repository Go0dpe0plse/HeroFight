import math

class Hero():
    def __init__(self, playername, name, hp, attack, mana):
        self.playername = playername
        self.name = name
        self.hp = hp
        self.attack = attack
        self.mana = mana

    def print_stats(self):
        return f"Hp: {self.hp}, Attack: {self.attack}, Mana: {self.mana}"

class Wizard(Hero):
    def __init__(self):
        super().__init__("", "Чарівник", 10, 4, 10)

    def charge(self):
        self.attack = round(self.attack / 100 * 50 + self.attack)

    def charge_off(self):
        self.attack = 4

class Sworder(Hero):
    def __init__(self):
        super().__init__("", "Мечник", 15, 3, 3)

    def charge(self):
        self.attack = round(self.attack / 100 * 50 + self.attack)

    def charge_off(self):
        self.attack = 3

def choose_hero(player_name):
    while True:
        choice = int(input(f"{player_name} обирає героя (1 або 2): 1 - {a.name}, 2 - {b.name}"))
        if choice == 1:
            return Sworder()
        elif choice == 2:
            return Wizard()
        else:
            print("Обирайте цифрами 1 або 2!")

def perform_action(player, opponent):
    action = int(input("Удар або Заряд. (1 & 2): "))
    if action == 1:
        print(f"{player.name} Наносить удар!")
        opponent.hp -= player.attack
        print(f"Здоров'я противника = {opponent.hp}")
        player.charge_off()
    elif action == 2:
        player.charge()
        print(f"Наступна атака = {player.attack}")

def game_round(player1, player2):
    for player, opponent in [(player1, player2)]:
        print(f"\nХід гравця: {player.playername}")
        perform_action(player, opponent)
        if opponent.hp <= 0:
            print(f"{player.playername} вітаємо з перемогою!")
            return True
    return False

a = Sworder()
b = Wizard()

name_player1 = input("Як тебе звати, гравець один?")
name_player2 = input("Як тебе звати, гравець два?")

player_one = choose_hero(name_player1)
player_one.playername = name_player1
player_two = choose_hero(name_player2)
player_two.playername = name_player2

round_number = 1

while True:
    print(f"\nРаунд {round_number}")
    if game_round(player_one, player_two):
        break
    if game_round(player_two, player_one):
        break
    round_number += 1
