import os
import csv

couriers_keys = ["name", "phone"]

def clear():
    os.system( 'cls' )

def open_courier_file(couriers_list):
    try:
        with open("couriers.csv", "r") as couriers_file:
            couriers_in_file = csv.DictReader(couriers_file)
            for row in couriers_in_file:
                couriers_list.append(row)
    except:
        print('Failed to open file')

def update_courier_file(couriers_list):
    try:
        with open('couriers.csv', 'w', newline='') as couriers_file:
            couriers_in_file = csv.DictWriter(couriers_file, fieldnames = couriers_keys)
            couriers_in_file.writeheader()
            couriers_in_file.writerows(couriers_list)
    except:
        print('Failed to open file')

def show_couriers(couriers_list):
    clear()
    print("Couriers available:\n")
    for courier in couriers_list:
        courier_index = couriers_list.index(courier)
        print(f"Courier Number: {courier_index}")
        for key, value in courier.items():
            print(f"{key} : {value}")
        print("______________________________")

def add_new_courier(couriers_list):
    new_courier = {}
    new_courier["name"] = input("Courier Name: ")
    new_courier["phone"] = input("Courier phone number: ")
    couriers_list.append(new_courier)

def edit_existing_courier(couriers_list):
    print(f"Would you like to edit an existing courier? \n")
    print("Options: \n Return to main menu (type 0) | Edit existing courier (type 1) \n ")
    
    try:
        edit_options = int(input("Would you like to continue editing an existing courier? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1: 
        clear()  
        show_couriers(couriers_list)
        try:
            edit_input_index = int(input("Which courier would you like to edit? \n please enter the courier number - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if edit_input_index >= 0 and edit_input_index <= len(couriers_list):
            clear()
            print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
            
            new_courier_name = input("Courier name: ").lower()
            if new_courier_name != "":
                couriers_list[edit_input_index]["name"] = new_courier_name
            
            new_product_price = input("Courier phone number: ")
            if new_product_price != "":
                couriers_list[edit_input_index]["phone"] = new_product_price
        else:
            clear()
            print("That was an invalid product number")
    else:
        clear()
        print("That was an invalid input")

def delete_courier(couriers_list):
    print(f"Would you like to remove a courier? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing courier (type 1) \n ")
    
    try:
        delete_options = int(input("Would you like to continue removing a courier? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        clear()
        show_couriers(couriers_list)
        
        try:
            delete_courier_index = int(input("Please enter the courier number of the product you wish to delete - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if delete_courier_index >= 0 and delete_courier_index <= len(couriers_list):
            del couriers_list[delete_courier_index]
        else:
            clear()
            print("Courier {delete_courier_index} does not exist.")
    else:
        clear()
        print("That was an invalid input")
