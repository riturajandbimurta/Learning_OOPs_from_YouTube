class chatbook:

    def __init__(self):
        self.username = ' '
        self.password = ' '
        self.loggedin = False
        self.menu()
    

    def menu(self):
        user_input = input(""""Welcome to chatbook how would u like to proceed
                        1. Press 1 to sign up 
                        2. press 2 to sign in 
                        3. press 3 to write a post 
                        4. press 4 to message a friend 
                        5. press any other key to exit""")
        if  user_input == 1:
            pass
        elif user_input ==2:
            pass 
        elif user_input ==3:
            pass 
        elif user_input ==4:
            pass 
        elif user_input ==5:
            pass 
        else:
            exit()

obj = chatbook()