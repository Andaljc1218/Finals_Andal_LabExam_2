import os

class userManager:
    
    def __init__(self):
        self.acc_lib = {}
        self.current_user = None
        self.data_folder = "data"
        self.data_file = "user.txt"
        self.load_users()


    def load_users(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

        path = os.path.join(self.data_folder, self.data_file)

        if not os.path.exists(path):
            open(path, 'w').close() 
        else:
            with open(path, 'r') as file:
                for line in file:
                    username, password = line.strip().split(', ')
                    self.acc_lib[username] = password
        
    def save_users(self):
        path = os.path.join(self.data_folder, self.data_file)
        
        with open(path, 'w') as file:
            
            for username, password in self.acc_lib.items():
                file.write(f"{username}, {password}\n")
                
    def validate_username(self, username):
        if len(username) <= 3:
            return False
        else:
            return True
    def validate_password(self, password):
        if len(password) <= 7:
            return False
        else:
            return True
        
    def register(self, username, password):
        if username in self.acc_lib:
            print("\n========================================")
            print("         Username already exist. ")
            print("========================================\n")
            return False
            
        self.acc_lib[username] = password
        self.save_users()
        return True
             
    def login(self, username, password):
        if username in self.acc_lib and self.acc_lib[username] == password:
            self.current_user = username
            return True, self.current_user
        else:
            return False
        

        
        
        