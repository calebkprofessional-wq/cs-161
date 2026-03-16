
class Character:
    def __init__(self, name, health=10):
        self.name = name
        self.health = health

    def health_report(self):
        print(f"\n{self.name} has health {self.health}.")

class Witch(Character):
    def __init__(self, name, health=10):
        super().__init__(name, health)

    def spell(self):
        print(f"\n{self.name} uses Swoosh")
        self.health = self.health - 1

class Warlock(Character):
    def __init__(self, name, health=10):
        super().__init__(name, health)

    def spell(self):
        print(f"\n{self.name} uses Kaboom!")
        self.health = self.health - 2

glenda = Witch('Glenda')
goliath = Warlock('Goliath')

glenda.spell()
glenda.health_report()
glenda.spell()
glenda.health_report()
glenda.spell()
glenda.health_report()

goliath.spell()
goliath.health_report()
goliath.spell()
goliath.health_report()
goliath.spell()
goliath.health_report()
