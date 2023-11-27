class Fighter:
    def __init__(self, name, health, damagePerAttack):
        self.__name = name
        self.__health = health
        self.__damagePerAttack = damagePerAttack

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_damagePerAttack(self):
        return self.__damagePerAttack

    def set_name(self, value):
        self.__name = value

    def set_health(self, value):
        self.__health = value

    def set_damagePerAttack(self, value):
        self.__damagePerAttack = value

    def is_alive(self):
        return self.__health > 0


class Fight:
    def __init__(self, figher1: Fighter, figher2: Fighter):
        self.figher1 = figher1
        self.figher2 = figher2

    def fight(self):
        while self.figher1.is_alive() and self.figher2.is_alive():
            self.figher2.set_health(self.figher2.get_health() - self.figher1.get_damagePerAttack())
            if not self.figher2.is_alive():
                return self.figher1.get_name()
            self.figher1.set_health(self.figher1.get_health() - self.figher2.get_damagePerAttack())
            if not self.figher1.is_alive():
                return self.figher2.get_name()


def main():
    fighter1 = Fighter("Max",150, 25)
    fighter2 = Fighter("Ben", 135, 20)

    fight = Fight(fighter1, fighter2)
    winner = fight.fight()
    print(f"The winner is {winner}")


if __name__ == '__main__':
    main()

