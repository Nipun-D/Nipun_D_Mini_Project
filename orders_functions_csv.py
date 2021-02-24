import csv
import os
from couriers_functions import show_couriers

orders_keys = ["customer_name", "customer_address", "customer_phone", "courier", "status", "items"]

def clear():
    os.system( 'cls' )

def open_orders_file(orders_list):
    try:
        with open("orders.csv", "r") as orders_file:
            orders_in_file = csv.DictReader(orders_file)
            for row in orders_in_file:
                orders_list.append(row)
    except:
        print('Failed to open file')

def update_orders_file(orders_list):
    try:
        with open('orders.csv', 'w', newline='') as orders_file:
            orders_in_file = csv.DictWriter(orders_file, fieldnames = orders_keys)
            orders_in_file.writeheader()
            orders_in_file.writerows(orders_list)
    except Exception as e:
        print(f'Failed to open file {e}')

def show_orders(orders_list):
    clear()
    print("Current Orders:\n")
    for order in orders_list:
        order_index = orders_list.index(order)
        print(f"Order Number: {order_index}")
        for key, value in order.items():
            print(f"{key} : {value}")
        print("___________________________________________________________")

def add_new_order(orders_list, couriers_list):
    new_order = {}
    list_items = []
    
    new_order["customer_name"] = input("Customer Name: ")
    
    new_order["customer_address"] = input("Customers Full Address: ")
    
    new_order["customer_phone"] = input("Customer Phone Number: ")
    
    print("Courier available:")
    
    show_couriers(couriers_list)
    new_courier = input("\nCourier Number: ")
    new_order["courier"] = int(new_courier)
    
    new_order["status"] = "preparing"
    
    number_of_items = int(input("How many items would you like to add to the order? "))
    for i in range(0, number_of_items):
        item = int(input("Item number of the item you wish to add -"))
        list_items.append(item)
    new_order["items"] = list_items
    
    orders_list.append(new_order)

def update_order_status(orders_list):
    print("Updating order status")
    print("Options: \n Cancel (type 0) | Edit order status (type 1) \n ")
    
    try:
        status_order = int(input("Would you still like to update an order status? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if status_order == 0:
        clear()
        return None
    elif status_order == 1:
        clear()
        show_orders(orders_list)
        
        try:
            order_status_order_number = int(input("Which order would you like to change the status of? "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if order_status_order_number >= 0 and order_status_order_number <= len(orders_list):
            new_order_status = input("Status options: Preparing | Delivered: ".lower())
            orders_list[order_status_order_number]["status"] = new_order_status
        else:
            clear()
            print(f"Can not find the order number {order_status_order_number}")
    else:
        clear()
        print("That was an invalid input")

def edit_existing_order(orders_list, couriers_list):
    print("\nOptions: \n Return to main menu (type 0) | Edit existing courier (type 1) \n ")
    
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
        show_orders(orders_list)
        
        try:
            edit_input_index = int(input("Which order would you like to edit? \n please enter the order number - "))
        except:
            clear()
            print("That was an invalid input")
            continue
        
        if edit_input_index >= 0 and edit_input_index <= len(orders_list):
            clear()
            print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
            
            new_cusotmer_name = input("Customer name: ")
            if new_cusotmer_name != "":
                orders_list[edit_input_index]["customer_name"] = new_cusotmer_name
            
            new_cusotmer_address = input("Customer adress: ")
            if new_cusotmer_address != "":
                orders_list[edit_input_index]["customer_address"] = new_cusotmer_address
            
            new_cusotmer_phone = input("Customer phone number: ")
            if new_cusotmer_phone != "":
                orders_list[edit_input_index]["customer_phone"] = new_cusotmer_phone
            
            show_couriers(couriers_list)
            new_courier = input("Courier number: ")
            if new_courier != "":
                orders_list[edit_input_index]["courier"] = int(new_courier)
            
            orders_list[edit_input_index]["status"] = "preparing"
            
            item_list = []
            print("NOTE: if you wish to keep existing items in the order please ADD them to this update. ")
            number_of_items = input("How many items will there be in this order?")
            if number_of_items != "":
                int_number_of_items = int(number_of_items)
                for i in range(0, int_number_of_items):
                    item = int(input("Item number of the item you wish to add -"))
                    item_list.append(item)
                orders_list[edit_input_index]["items"] = item_list
        else:
            clear()
            print(f"The order number {edit_input_index} is not available. ")
    else:
        clear()
        print("That was and invalid input")

def delete_order(orders_list):
    print("Would you like to delete an order?")
    print("Options: \n Return to main menu (type 0) | Remove existing order (type 1) \n ")
    
    try:
        delete_options = int(input("Would you like to continue removing an order? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        clear()
        show_orders(orders_list)
        
        try:
            delete_order_index = int(input("Please enter the order number of the order you wish to delete - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if delete_order_index >= 0 and delete_order_index <= len(orders_list):
            del orders_list[delete_order_index]
        else:
            clear()
            print("Order {delete_order_index} does not exist.")
    else:
        clear()
        print("That was an invalid input.")


# customer_name, customer_address, customer_phone, courier, status
# John,"Unit 12, 12 Main Street, LONDON, WH1 2ER",0789887334,2,preparing
# Bob,"Unit 11, 11 Main Street, LONDON, WH2 5ER",0789882222,3,preparing