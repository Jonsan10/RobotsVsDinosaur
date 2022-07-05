class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack(self, Robot):
        robot_health = 100
        print(f'The{self.name} attacked the {Robot} for {self.attack_power}')
        robot_health -= self.attack_power
        print(f'the robots health decreased to{robot_health}')

   