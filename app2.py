import sys
from functions_file import *

print('Welcome to the app!')

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
            products = add_new_product()
        
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
        