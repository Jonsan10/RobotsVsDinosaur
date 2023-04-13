class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, robot):
        print(f'The Dino{self.name} attacked the {robot.name} for {self.attack_power}')
        robot.health -= self.attack_power
        print(f'the robots health decreased to{robot.health}')

   