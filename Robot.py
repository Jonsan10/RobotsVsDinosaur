from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('Blaster', 10)

    def attack(self, dinosaur ):
         dinosaur_health = 100
         active_weapon = Weapon
         dinosaur_health -= active_weapon

         print(f'{self.name} attacked {dinosaur} and dealt {self.active_weapon} to the dinosaur.')
         dinosaur_health -= self.active_weapon
         print(f'the dinosaurs health decreased to {dinosaur_health}')

        












# little_foot = {}

# r2d2 = Robot('R2D2', Weapon('Blaster', 21))

# r2d2.attack(little_foot)