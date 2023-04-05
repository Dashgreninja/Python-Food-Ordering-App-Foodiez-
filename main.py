from foodiez_functions import *

class Main:
    def execute(self,log_choice):
        if log_choice == 1:
            log.admin_login()
                
        elif log_choice == 2:
            
            while True:
                print("\n+---------------------------------------+\n|Enter 1 to Register                    | \n|Enter 2 to Login if already Registered |\n+---------------------------------------+")
                reg_choice = int(input("Enter Your Choice :- "))
                if reg_choice == 1:
                    log.register()
                elif reg_choice == 2:
                    log.user_login()
                else:
                    print("Invalid Choice")
                

        else:
            print('See You Soon ')
            exit()
     
                
print("                                          Welcome To Foodiez")
print("+--------------------------+\n|Enter 1 to Login as Admin | \n|Enter 2 to Login as User  |\n+--------------------------+\n")
log_choice = int(input("Enter your choice :- "))
main = Main()
main.execute(log_choice)
# Change Path in foodiez_functions.py in class file_path to Run Program
