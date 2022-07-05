import Robot
import Dinosaur


class Battlefield:

    def _init_(self):
     self.robot = Robot('buzz')
     self.dinosaur = Dinosaur('mel', 20)

    def Run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaur')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        

    def display_winner():
        if Robot.health <= 0:
            print(' The winner is {self.Dinosaur_name}')

        elif Dinosaur.health <=0:
            print('The winner is {self.Robots_name}')

