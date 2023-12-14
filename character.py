class Character:
  def __init__(self, name, health=100, damage=3, defence=0):
      self.name = name
      self.health = health
      self.damage = damage
      self.defence = defence

  def __str__(self):
      return f'Ім\'я: {self.name}\n' \
             f'Здоров\'я: {self.health}\n' \
             f'Шкода: {self.damage}\n' \
             f'Захист: {self.defence}'

  def take_damage(self, damage):
      damage = max(damage - self.defence, 0)
      self.health -= damage
      return damage

  def attack(self, target):
      return target.take_damage(self.damage)

  def is_alive(self):
      return self.health > 0