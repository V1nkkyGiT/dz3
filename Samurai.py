from Lesson_3.character import Character

class Samurai(Character):
    def __init__(self, name, health=100, damage=3, defence=0):
        super().__init__(name, health, damage, defence)
        self.max_health = health
        self.attack_count = 0

    def count_damage(self):
        return self.damage * (2 - self.health / self.max_health)

    def special_ability(self, target):
        self.attack_count += 1
        if self.attack_count <= 5:  # Максимум 5 ударів
            self.damage *= 1.1  # Додаємо 10% до базової шкоди
        else:
            self.attack_count = 0  # Обнулюємо лічильник після 5 ударів

    def attack(self, target):
        self.special_ability(target)  # Викликаємо особливу механіку перед атакою
        return target.take_damage(self.count_damage())
