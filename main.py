from foodiez_functions import Main

                
print("                                          Welcome To Foodiez")
print("+--------------------------+\n|Enter 1 to Login as Admin | \n|Enter 2 to Login as User  |\n+--------------------------+\n")
log_choice = int(input("Enter your choice :- "))
main = Main()
main.execute(log_choice)
# Change Path in foodiez_functions.py in class file_path to Run Program
