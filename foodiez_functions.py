import json

# Change Path in file_path to Run Program
class file_path:
    food_items = "/Users/macbook/Documents/python files/python final project/food_items.json"
    user_pass = "/Users/macbook/Documents/python files/python final project/user_pass.json"
    order_history = "/Users/macbook/Documents/python files/python final project/order_history.json"

class Choice:
    def admin_choice(self,oper_choice):
        
        if oper_choice == 1:
            foodiez_func.add_items()
        elif oper_choice == 2:
            foodiez_func.edit_items()
        elif oper_choice == 3:
            foodiez_func.view_items()
        elif oper_choice == 4:
            foodiez_func.remove_items()
        elif oper_choice == 5:
            exit() 
            
    def user_choice(self,oper_choice,name):
        
        if oper_choice == 1:
            foodiez_user_func.place_oder(name)
        elif oper_choice == 2:
            foodiez_user_func.order_history(name)
        elif oper_choice == 3:
            foodiez_user_func.update_profile(name)
        elif oper_choice == 4:
            exit() 

class Foodiez_Admin_function:
    
    read_file = open(file_path.food_items,"r+")
    file_data = json.load(read_file)
    def add_items(self):
        
        if len(self.file_data['Menu Items']) == 0:
            ID = 1
        else:
            ID = self.file_data['Menu Items'][-1]['ID'] + 1
        Name = input("Enter Food Name : ")
        Quantity = input("Enter Food Quantity : ")
        Price = float(input("Enter Food Price : "))
        Discount = float(input("Enter Discount Given : "))
        Stock = int(input("Enter Stock : "))
        dict_obj = {
                    "ID":ID,
                    "Name":Name,
                    "Quantity":Quantity,
                    "Price":Price,
                    "Discount":Discount,
                    "Stock":Stock
            }
        
        self.file_data['Menu Items'].append(dict_obj)
        write_file = open(file_path.food_items,"w")
        json.dump(self.file_data,write_file)
        print("\nFood Item Successfully Added!")


    def edit_items(self):
        
        for i in self.file_data['Menu Items']:
            print(i,'\n')
            
        ID =int(input("\nEnter ID Of Item To Edit from above Items list :  "))
        for i in range(len(self.file_data['Menu Items'])):
            if ID == self.file_data['Menu Items'][i]['ID']:
                print('\n',self.file_data['Menu Items'][i])
                print("\n+------------------------------+\n|Enter 1 to Edit Food Name     | \n|Enter 2 to Edit Food Quantity | \n|Enter 3 to Edit Food Price    |\n|Enter 4 to Edit Discount      |\n|Enter 5 to Edit Stock         |\n+------------------------------+\n")
                edit_choice = int(input("\nEnter Your Choice : "))
                new_value = input("\nEnter New Value :")
                if edit_choice == 1:
                    self.file_data['Menu Items'][i]['Name'] = str(new_value)
                    print("\nFood Item Successfully Updated!")
                elif edit_choice == 2:
                    self.file_data['Menu Items'][i]['Quantity'] = str(new_value)
                    print("\nFood Item Successfully Updated!")
                elif edit_choice == 3:
                    self.file_data['Menu Items'][i]['Price'] = int(new_value)
                    print("\nFood Item Successfully Updated!")
                elif edit_choice == 4:
                    self.file_data['Menu Items'][i]['Discount'] = float(new_value)
                    print("\nFood Item Successfully Updated!")
                elif edit_choice == 5:
                    self.file_data['Menu Items'][i]['Stock'] = int(new_value)
                    print("\nFood Item Successfully Updated!")
                else:
                    print('Invalid Choice')
        
        write_file = open(file_path.food_items,"w")
        json.dump(self.file_data,write_file)
                    
            
            
    def view_items(self):
        
        for i in self.file_data['Menu Items']:
            print(i,'\n')
            
    def remove_items(self):
        
        for i in self.file_data['Menu Items']:
            print(i,'\n')
            
        ID =int(input("\nEnter ID Of Item To Remove from above Items list :  "))
        for i in range(len(self.file_data['Menu Items'])):
            if ID == self.file_data['Menu Items'][i]['ID']:
                del self.file_data['Menu Items'][i]
                print("\nFood Item Successfully Removed")
        write_file = open(file_path.food_items,"w")
        json.dump(self.file_data,write_file)

class Log:
    
    file = open(file_path.user_pass)
    file_data = json.load(file)
    def admin_login(self):
        
        user = input('\nAdmin Enter Username : ')
        pwd = input('Enter Password : ')
        if (user == self.file_data["Admin"]["Username"] and pwd == self.file_data["Admin"]["Password"]):
            while True:
                print("\n+---------------------------------------------------------+\n|Enter 1 to Add new food items                            | \n|Enter 2 to Edit food items using FoodID                  | \n|Enter 3 to View the list of all food items               |\n|Enter 4 to Remove a food item from the menu using FoodID |\n|Enter 5 to exit                                          |\n+---------------------------------------------------------+\n")
                oper_choice = int(input("Enter your choice :- "))
                choice.admin_choice(oper_choice)
        else:
            print('Wrong Username or Password')
        
    def register(self):
        
        Name = input("Enter Full Name : ")
        Phone_Number = int(input("Enter Phone Number : "))
        Email = input("Enter Email : ")
        Address = input("Enter Address : ")
        Password = input("Enter Password : ")
        dict_obj = {
                    "Full Name":Name,
                    "Phone Number":Phone_Number,
                    "Email":Email,
                    "Address":Address,
                    "Password":Password
            }
                
        self.file_data['Users'].append(dict_obj)
        write_file = open(file_path.user_pass,"w")
        json.dump(self.file_data,write_file)
        print("\nSuccessfully Registered!")
    
    def user_login(self):
        
        user_phone = input('\nEnter Your Full Name : ')
        pwd = input('Enter Password : ')
        for i in self.file_data['Users']:
            if (user_phone == i['Full Name'] and pwd == i['Password']):
                while True:
                    print("\n+------------------------------+\n|Enter 1 to Place New Order    | \n|Enter 2 to View Order History | \n|Enter 3 to Update Profile     |\n|Enter 4 to Exit               |\n+------------------------------+\n")
                    oper_choice = int(input("Enter your choice :- "))
                    choice.user_choice(oper_choice,i['Full Name'])
        else:
            print('Wrong Username or Password')

class Foodiez_User_Function():
    read_file = open(file_path.food_items,"r+")
    file_data = json.load(read_file)
    def place_oder(self,name="Dushyant Pratap"):
        print("\n\t\tMenu\n")
        for i in self.file_data["Menu Items"]:
            print( f'{i["ID"]}  {i["Name"]}   ({i["Quantity"]})   INR[{i["Price"]}]\n')
        food_choice = input('Enter Your Choice in [1,2,....] format : ')
        dict_obj = {
                    name:{
                    }
            }
        count=1
        for j in food_choice:
            if j.isdigit():
               
                dict_obj[name][count] = self.file_data["Menu Items"][int(j)-1]
                count+=1
        print("\n Selected Items ")
        for i in dict_obj[name]:
                print( f'\n{i}  {dict_obj[name][i]["Name"]}   ({dict_obj[name][i]["Quantity"]})   INR[{dict_obj[name][i]["Price"]}]\n')            
        confirm = int(input("Enter 1 to Place Order or 2 to Exit : "))    
        if confirm == 1:
            print("\nOrder Placed!")
            order_history_file = open(file_path.order_history,"r+")
            new_data = json.load(order_history_file)
            new_data['History'].append(dict_obj)
            write_file = open(file_path.order_history,"w")
            json.dump(new_data,write_file)
        else:
            print("\nSee You Soon")
              
    def order_history(self,name):
        order_history_file = open(file_path.order_history,"r+")
        new_data = json.load(order_history_file)
        print('\nYour Order History :')
        for i in new_data["History"]:
            for open_i in i:
                if open_i == name:
                    for j in i.values():
                        for k in j.values():
                            print( f'\n{k["Name"]}   ({k["Quantity"]})   INR[{k["Price"]}]')
                
    def update_profile(self,name):
        file = open(file_path.user_pass)
        read_profile = json.load(file)
        
        for i in range(len(read_profile['Users'])):
            if name == read_profile['Users'][i]['Full Name']:
                print('\n',read_profile['Users'][i])
                print("\n+-----------------------------+\n|Enter 1 to Edit Full Name    | \n|Enter 2 to Edit Phone Number | \n|Enter 3 to Edit Email        |\n|Enter 4 to Edit Address      |\n|Enter 5 to Password          |\n+-----------------------------+\n")
                edit_choice = int(input("\nEnter Your Choice : "))
                new_value = input("\nEnter New Value :")
                if edit_choice == 1:
                    read_profile['Users'][i]['Full Name'] = str(new_value)
                    print("\nInfo Successfully Updated!")
                elif edit_choice == 2:
                    read_profile['Users'][i]['Phone Number'] = int(new_value)
                    print("\nInfo Successfully Updated!")
                elif edit_choice == 3:
                    read_profile['Users'][i]['Email'] = str(new_value)
                    print("\nInfo Successfully Updated!")
                elif edit_choice == 4:
                    read_profile['Users'][i]['Address'] = str(new_value)
                    print("\nInfo Item Successfully Updated!")
                elif edit_choice == 5:
                    read_profile['Users'][i]['Password'] = str(new_value)
                    print("\nInfo Successfully Updated!")
                else:
                    print('Invalid Choice')
                    
        write_file = open(file_path.user_pass,"w")
        json.dump(read_profile,write_file)
        exit()

       
choice = Choice()
foodiez_func = Foodiez_Admin_function()
log = Log()
foodiez_user_func = Foodiez_User_Function()
