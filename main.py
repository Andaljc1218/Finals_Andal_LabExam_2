import sys
from utils.user_manager import userManager
from utils.dice_game import DiceGame

user_manager = userManager()
dice_game = DiceGame() 

def main():
    
    while True:
        try:
            print("\nWelcome to Dice Roll Game!\n")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                print("\n========================================")
                print("Registration\n")
                username = str(input("Enter username at least 4 characters long, or leave blank to cancel: "))
                if username == "" or username == " ":
                    main()
                    return
                elif not user_manager.validate_username(username):
                    print("\n========================================")
                    print(" Username must be at least 4 characters")
                    print("========================================")
                    main()
                    return
                
                password = str(input("Enter password at least 8 characters long, or leave blank to cancel: "))
                if password == "" or password == " ":
                    main()
                    return
                elif not user_manager.validate_password(password):
                    print("\n========================================")
                    print(" Password must be at least 8 characters")
                    print("========================================")
                    main()
                    return
        

                if user_manager.register(username, password):
                    print("\n========================================")
                    print("        Registration successful")
                    print("========================================")

            elif choice == "2":
                print("\n========================================")
                print("Login\n")
                username = input("Enter username, or leave blank to cancel: ")
                if username == "" or username == " ":
                    return
                password = input("Enter password, or leave blank to cancel: ")   
                if password == "" or password == " ":
                    return

                if user_manager.login(username, password):
                    current_user = user_manager.current_user
                    print("\n========================================")
                    print("           Log in successful.")
                    print("========================================")
                    dice_game.menu(current_user)
                else:
                    print("\n========================================")
                    print("           Account not found")
                    print("========================================")
                    main()
                    return

            elif choice == "3":
                print("Exiting program...Thank you for playing!")
                sys.exit()
            else:
                print("\n========================================")
                print("   Invalid choice. Please try again")
                print("========================================")
        except ValueError:
            print("\nWrong input")
            break

main()