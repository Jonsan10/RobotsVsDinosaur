import Robot
import Dinosaur


player_1 = Robot
player_2 = Dinosaur

class Battlefield:

    def _init_(self):
     self.robot = Robot
     self.dinosaur = Dinosaur

    def Run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaur')

    def battle_phase(self):
        choice_1 =(self.Robots_name)
        choice_2 = (self.Dinosaur_name)

        if self.robots_health <= 0
        

   # def display_winner():
        if Robot.health <= 0:
            print(' The winner is {self.Dinosaur_name}')

        elif Dinosaur.health <=0:
            print('The winner is {self.Robots_name}')

