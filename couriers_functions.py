import os

def clear():
    os.system( 'cls' )

def open_courier_file(couriers):
    try:
        with open("couriers.txt",'r') as couriers_file:
            couriers_in_file = couriers_file.readlines()
            for courier in couriers_in_file:
                couriers.append(courier.rstrip())
    except:
        print('Failed to open file')

def update_courier_file(couriers):
    try:
        with open("couriers.txt",'w') as couriers_file:
            for courier in couriers:
                couriers_file.write(courier + '\n')
    except:
        print('Failed to open file')

def add_new_courier(couriers):
    add_courier = input("What product would you like to add? ").lower()
    couriers.append(add_courier)

def edit_existing_courier(couriers):
    print(f"Couriers available to edit: {couriers} \n Would you like to edit an existing courier? \n")
    print("Options: \n Return to main menu (type 0) | Edit existing courier (type 1) \n ")
    edit_options = int(input("Would you like to continue editing an existing courier? "))
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1: 
        clear()
        for (i, item) in enumerate(couriers, start=1):
            print(i, item)
        edit_input_index = int(input("Which courier would you like to edit? \n please enter the number they appears in the list - "))
        if edit_input_index >= 0 and edit_input_index <= len(couriers): 
            edit_input_courier = input("Enter the new courier name: ").lower()
            couriers[edit_input_index-1] = edit_input_courier
        else:
            clear()
            print("That is an invalid courier number")
    else:
        clear()
        print("That was an invalid input")

def delete_courier(couriers):
    print(f"Couriers available to remove: {couriers} \n Would you like to remove a courier? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing courier (type 1) \n ")
    delete_options = int(input("Would you like to continue removing a courier? "))
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        delete_input_courier = input("Which courier would you like to remove? ").lower()
        if delete_input_courier in couriers:
            couriers.remove(delete_input_courier)
        else:
            clear()
            print("Can not find the courier {delete_input_courier}.")
    else:
        clear()
        print("That was an invalid input")
