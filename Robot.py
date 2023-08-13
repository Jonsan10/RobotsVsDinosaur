from weapon import Weapon

lazer_hands = Weapon('Laser hands', 25)
hook_hooves = Weapon('Hook hooves', 15)
blaster = Weapon('Blaster', 10)

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = None 

    def choose_weapon(self):
        print(f'{self.name}, Please select which weapon to attack with')
        print('Enter 1 for Laser hands, Enter 2 for the Hook Hooves, or Enter 3 for the Blaster')
        user_input = int(input('Which Weapon would you like to take into battle: '))
        if user_input == 1:
            self.active_weapon = lazer_hands
        elif user_input == 2:
            self.active_weapon = hook_hooves
        elif user_input == 3:
            self.active_weapon = blaster
        else:
            print('Not a valid Choice')

    def attack(self, dinosaur):
        if self.active_weapon is None:
            print(f'{self.name} has no active weapon to attack with.')
            return

        print(f'Robot {self.name} attacked {dinosaur.name} with {self.active_weapon.name} for {self.active_weapon.attack_power} to the dinosaur.')
        dinosaur.health -= self.active_weapon.attack_power
        print(f'the dinosaur\'s health decreased to {dinosaur.health}')













# little_foot = {}

# r2d2 = Robot('R2D2', Weapon('Blaster', 21))

# r2d2.attack(little_foot)