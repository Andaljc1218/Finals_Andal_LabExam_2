from .user_manager import userManager
from .score import Score
from .user import User

import uuid
import os
import random

user_manager = userManager()
score = Score()
user =  User()

class DiceGame:
    
    def __init__(self):
        self.user_manager = user_manager
        self.score = Score()
        self.data_folder = "data"
        self.data_file = "rankings.txt"
        self.load_scores()
        

    def load_scores(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)
        
        path = os.path.join(self.data_folder, self.data_file)
        
        if not os.path.exists(path):
            with open(path, 'w') as file:
                file.write("Username -- Game ID -- Points -- Wins\n")

    def save_scores(self):

        path = os.path.join(self.data_folder, self.data_file)
        with open(path, 'a') as file:
                file.write(f"{self.score.username}   --   {self.score.game_id}   --   {self.score.points}   --   {self.score.wins}\n")
        
    def play_game(self, current_user):
        game_id = str(uuid.uuid4())[:5]

        print("\n========================================")
        print(f"Starting the game as {current_user}\n")
        total_points = 0
        stages_won = 0
        cpu_wins = 0
        cpu_points = 0

        while True:
            stage_points = 0

            for _ in range(3):
                current_user_roll = random.randint(1,6)
                cpu_roll = random.randint(1,6)

                print(f"{current_user} rolled: {current_user_roll}")
                print(f"CPU rolled: {cpu_roll} ")

                if current_user_roll > cpu_roll:
                    print("================================")
                    print(f"  You win this round! {current_user}")
                    print("================================\n")
                    stage_points += 1
                    total_points += 1

                elif current_user_roll < cpu_roll:
                    print("================================")
                    print("     CPU wins this round!")
                    print("================================\n")
                    cpu_wins += 1
                    cpu_points += 1
                else:
                    print("================================")
                    print("          It's a tie!")
                    print("================================\n")

            if stage_points == 1 and cpu_wins == 1:
                print("The stage is draw.\n")
                continue

            elif stage_points >= 2:
                print(f"You won this stage {current_user}")
                total_points += 3
                stages_won += 1
                print(f"Total points: {total_points}, Stages won: {stages_won}\n")

                choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")

                while choice not in ['1', '0']:
                    print("Invalid input. Please enter 1 for Yes or 0 for No.\n")
                    choice = input("Do you want to continue to the next stage? (1 for Yes, 0 for No): ")

                if choice == '1':
                    continue
                elif choice == '0':
                    print(f"\nGame over! Thank you for playing {current_user}.")
                    self.score.username = current_user
                    self.score.game_id = game_id
                    self.score.points = total_points
                    self.score.wins = stages_won
                    self.save_scores()
                    self.menu(current_user)
                    return 
                

            elif cpu_points >= 2:
                print(f"You've lost this stage {current_user}!")
                print(f"Game over! You didn't win the stage.")
                self.score.username = current_user
                self.score.game_id = game_id
                self.score.points = total_points
                self.score.wins = stages_won
                self.save_scores()
                self.menu(current_user)
                return 
                

    def show_top_scores(self,current_user):
        path = os.path.join(self.data_folder, self.data_file)
        scores = []

        with open(path, 'r') as file:
            next(file)  # Skip header
            for line in file:
                username, _, points, wins = line.strip().split(" -- ")
                scores.append((username, int(points), int(wins)))

        scores.sort(key=lambda x: x[1], reverse=True)
        top_scores = scores[:10]

        if not top_scores:
            print("No scores available yet. Play a game to see top scores!")
            self.menu(current_user)
            return

        print("\nTop 10 Highest Scores:")
        for i, (username, points, wins) in enumerate(top_scores, start=1):
            print(f"{i}. {username}: Points: {points}, Wins: {wins}")
        self.menu(current_user)

    def logout(self, current_user):
        print("\n========================================")
        print(f"Goodbye, {current_user}! Logging out....")
        print("========================================") 
        return
    
    def menu(self, current_user):
        
        print("\n================================")
        print(f"Welcome, {current_user}!\n")
        print("Menu: ")
        print("1. Start game")
        print("2. Show top scores")
        print("3. Log out")

        choice = input("\nEnter your choice, or leave blank to cancel: ")

        if choice == "":
            return
        if choice == "1":
            self.play_game(current_user)
        elif choice == "2":
            self.show_top_scores(current_user)
        elif choice == "3":
            self.logout(current_user)
        else:
            print("\n========================================") 
            print("Invalid choice. Please try again.")
            print("========================================") 
            self.menu(current_user)
        



           




        

    
    