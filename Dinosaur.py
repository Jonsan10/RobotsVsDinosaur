class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        if hasattr(robot, 'health'):
            print(f'The Dino {self.name} attacked {robot.name} for {self.attack_power}')
            robot.health -= self.attack_power
            print(f"The robot's health decreased to {robot.health}")
        else:
            print(f'{robot.name} does not have a health attribute.')

