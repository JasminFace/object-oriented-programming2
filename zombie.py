import random

class Zombie:

  max_speed = 5
  horde = []
  plague_level = 10
  default_speed = 1
  max_strength = 8
  default_strength = 3

  def __init__(self, speed, strength):
    """Initializes zombie's speed and strength
    """
    if speed > Zombie.max_speed:
      self.speed = Zombie.default_speed
    else:
      self.speed = speed

    if strength > Zombie.max_strength:
        self.strength = Zombie.default_strength
    else:
        self.strength = strength
        
  def __str__(self):
    return f"Speed = {self.speed} Strength = {self.strength}"

  def fight(self):
    """Represents you trying to fight this particular zombie.
    Uses `Zombie.max_strength` to generate a random number that represents your strength when fighting the zombie.
    """
    your_strength = random.randint(1, Zombie.max_strength)
    return your_strength > self.strength

  @classmethod
  def spawn(cls):
    """Spawns a random number of new zombies, based on the plague level,
    adding each one to the horde.  Each zombie gets a random speed.
    """
    new_zombies = random.randint(1, Zombie.plague_level)
    count = 0

    while count < new_zombies:
      speed = random.randint(1, Zombie.max_speed)
      strength = random.randint(1, Zombie.max_strength)
      Zombie.horde.append(Zombie(speed, strength))
      count += 1

  @classmethod
  def new_day(cls):
    """Represents the events of yet another day of the zombie apocalypse.
    Every day some zombies die off (phew!), some new ones show up,
    and sometimes the zombie plague level increases.
    """
    Zombie.spawn()
    Zombie.some_die_off()

  @classmethod
  def some_die_off(cls):
    """Removes a random number (between 0 and 10) of zombies from the horde.
    """
    how_many_die = random.randint(0, 10)
    counter = 0
    while counter < how_many_die and len(Zombie.horde) > 0:
      random_zombie = random.randint(0,len(Zombie.horde) - 1)
      Zombie.horde.pop(random_zombie)
      counter += 1

  @classmethod
  def increase_plague_level(cls):
      new_plague_level = random.randint(0,2)
      Zombie.plague_level += new_plague_level

      cls.new_day()

  def encounter(self):
    """This instance method represents you coming across a zombie! This can end in:
    1. You outrun the zombie and escape unscathed!
    2. You don't outrun the zombie but enter battle and defeat the zombie!
    3. You don't outrun the zombie, you enter battle, but DIE. :(
    Returns a summary of what happened.
    """
    outrun = self.chase()
    battle = self.fight()

    if outrun == True:
        return 'You escaped!'
    elif outrun == False:
        if battle:
            Zombie.horde.append(self)
            return "You survived! But now you're a Zombie. =("
        else:
            return "You weren't strong enough. You died."

  def chase(self):
    """Represents you trying to outrun this particular zombie.
    Uses `Zombie.max_speed` to generate a random number that represents how fast you manage to run.
    """
    your_speed = random.randint(1, Zombie.max_speed)
    return your_speed > self.speed


print(Zombie.horde) # []

Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x109756d30>, <__main__.Zombie object at 0x10975f940>, <__main__.Zombie object at 0x10975fa20>, <__main__.Zombie object at 0x10975fac8>, <__main__.Zombie object at 0x10975fb00>]
zombie1 = Zombie.horde[0]
print(zombie1) # Speed = 3 Strength = 4
zombie2 = Zombie.horde[1]
print(zombie2) # Speed = 1 Strength = 7
print(zombie1.encounter()) # You survived! But now you're a Zombie. =(
print(zombie2.encounter()) # You escaped!

Zombie.new_day()
print(Zombie.horde) # [<__main__.Zombie object at 0x10975fa20>, <__main__.Zombie object at 0x109756d30>, <__main__.Zombie object at 0x10975f9e8>, <__main__.Zombie object at 0x10975fc50>, <__main__.Zombie object at 0x10975fcc0>, <__main__.Zombie object at 0x10975fcf8>]
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1) # Speed = 2 Strength = 5
print(zombie2) # Speed = 3 Strength = 4
print(zombie1.encounter()) # You weren't strong enough. You died.
print(zombie2.encounter()) # You escaped!