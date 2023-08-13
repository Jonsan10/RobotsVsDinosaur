from Robot import Robot
from Dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.robot = Robot('buzz')
        self.dinosaur = Dinosaur('mel', 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        
    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs')

    def battle_phase(self):
        self.robot.choose_weapon()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)
            self.robot.attack(self.dinosaur)
            if self.robot.health <= 0 or self.dinosaur.health <= 0:
                break
        
    def display_winner(self):
        if self.robot.health <= 0:
            print(f'The winner is {self.dinosaur.name}')
        elif self.dinosaur.health <= 0:
            print(f'The winner is {self.robot.name}')





