from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def _init_(self):
     self.robot = Robot('buzz')
     self.dinosaur = Dinosaur('mel', 20)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaur')

    def battle_phase(self):
        self.robot.choose_weapon()
        while self.robot.health > 0 and self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
                self.robot.attack(self.dinosaur)
                if self.robot.health <= 0 or self.dinosaur.health <= 0:
                    break
        

    def display_winner(self):
        if Robot.health <= 0:
            print(' The winner is {self.Dinosaur_name}')

        elif Dinosaur.health <=0:
            print('The winner is {self.Robots_name}')

