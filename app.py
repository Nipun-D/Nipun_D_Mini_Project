import sys
import os

# from functions_file import *

def clear():
    os.system( 'cls' )

print('Welcome to the Coffee House!')

products = []
couriers = []

def open_product_file():
    try:
        with open("products.txt",'r') as products_file:
            products_in_file = products_file.readlines()
            for product in products_in_file:
                products.append(product.rstrip())
    except:
        print('Failed to open file')

def open_courier_file():
    try:
        with open("couriers.txt",'r') as couriers_file:
            couriers_in_file = couriers_file.readlines()
            for courier in couriers_in_file:
                couriers.append(courier.rstrip())
    except:
        print('Failed to open file')

def update_product_file():
    try:
        with open("products.txt",'w') as products_file:
            for product in products:
                products_file.write(product + '\n')
    except:
        print('Failed to open file')

def update_courier_file():
    try:
        with open("couriers.txt",'w') as couriers_file:
            for courier in couriers:
                couriers_file.write(courier + '\n')
    except:
        print('Failed to open file')

def add_new_product():
    add_product = input("What product would you like to add? ").lower()
    products.append(add_product)

def edit_existing_product():
    print(f"Products available to edit: {products} \n Would you like to edit an existing product? \n")
    print("Options: \n Return to main menu (type 0) | Edit existing product (type 1) \n ")
    edit_options = int(input("Would you like to continue editing a product? "))
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1:
        clear()  
        for (i, item) in enumerate(products, start=1):
            print(i, item)
        edit_input_index = int(input("Which item would you like to edit? \n please enter the number it appears in the list - "))
        edit_input_product =input("Enter the new product name: ").lower()
        products[edit_input_index-1] = edit_input_product

def delete_product():
    print(f"Products available to remove: {products} \n Would you like to delete a product? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing product (type 1) \n ")
    delete_options = int(input("Would you like to continue removing a product? "))
    if delete_options == 0:
        clear()
        return None
    elif delete_options ==1:
        delete_input_product = input("Which product would you like to remove? ").lower()
        products.remove(delete_input_product)

def add_new_courier():
    add_courier = input("What product would you like to add? ").lower()
    products.append(add_courier)

def edit_existing_courier():
    print(f"Couriers available to edit: {couriers} \n Would you like to edit an existing courier? \n")
    print("Options: \n Return to main menu (type 0) | Edit existing courier (type 1) \n ")
    edit_options = int(input("Would you like to continue editing an existing courier? "))
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1: 
        clear()
        for (i, item) in enumerate(products, start=1):
            print(i, item)
        edit_input_index = int(input("Which courier would you like to edit? \n please enter the number they appears in the list - "))
        edit_input_product =input("Enter the new courier name: ").lower()
        products[edit_input_index-1] = edit_input_product

def delete_courier():
    print(f"Couriers available to remove: {couriers} \n Would you like to remove a courier? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing courier (type 1) \n ")
    delete_options = int(input("Would you like to continue removing a courier? "))
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        delete_input_product = input("Which courier would you like to remove? ").lower()
        products.remove(delete_input_product)

open_product_file()
open_courier_file()

while True:
    print('Options: \n Save & close app (type: 0) | Products Menu (type: 1) | Couriers Menu (type: 2)')
    input_for_main_menu = int(input("\n Select a menu option (0 | 1 | 2) - "))
    
    if input_for_main_menu == 0:
        clear()
        update_product_file()
        update_courier_file()
        print("Thank you for using the app")
        sys.exit(0)
    
    elif input_for_main_menu == 1:
        clear()
        print(f"\n Products available: {products}")
        print("\n Options: \n Return to menu (type: 0) | Show products (type: 1) | Add new product (type: 2) | \n Update existing product (type: 3) | Delete a product (type: 4)")
        
        input_second_options = int(input("\n Select a menu option (0 | 1 | 2 | 3 | 4) - "))
        
        if input_second_options == 0:
            clear()
            print("You have returned to the main menu \n")
        
        elif input_second_options == 1:
            clear()
            print(f"Products available: {products}")
        
        elif input_second_options == 2:
            clear()
            add_new_product()
        
        elif input_second_options == 3:
            clear()
            edit_existing_product()
        
        elif input_second_options == 4:
            clear()
            delete_product()
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    elif input_for_main_menu == 2:
        clear()
        print(f"\n Couriers available: {couriers}")
        print("\n Options: \n Return to menu (type: 0) | View couriers available (type: 1) | Add new courier (type: 2) |\n Update existing courier (type: 3) | Remove existing courier (type: 4)")
        
        input_third_options = int(input("\n Select a menu option (0 | 1 | 2 | 3 | 4) - "))
        
        if input_third_options == 0:
            clear()
            print("You have returned to the main menu \n ")
        
        elif input_third_options == 1:
            clear()
            print(f"Couriers available: {couriers}")
        
        elif input_third_options == 2:
            clear()
            add_new_courier()
        
        elif input_third_options == 3:
            clear()
            edit_existing_courier()
        
        elif input_third_options == 4:
            clear()
            delete_courier()
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    else:
        clear()
        print("That was not a valid option, please eneter a valid one.")