import sys
import os
import csv
from products_functions import *
from couriers_functions import *
from orders_functions import *

print('Welcome to the app!')

products = []
couriers = []
orders_list = []

def clear():
    os.system( 'cls' )

open_product_file(products)
open_courier_file(couriers)
open_orders_file(orders_list)

while True:
    
    print("\n Main Menu")
    print('Options: \n Save & close app (type: 0) | Products Menu (type: 1) | Couriers Menu (type: 2) | Orders Menu (type: 3)')
    input_for_main_menu = int(input("\n Select a menu option (0 | 1 | 2 | 3) - "))
    
    if input_for_main_menu == 0:
        clear()
        update_product_file(products)
        update_courier_file(couriers)
        update_orders_file(orders_list)
        print("Thank you for using the app")
        sys.exit(0)
    
    elif input_for_main_menu == 1:
        clear()
        print(f"\n Products Menu")
        print("\n Options: \n Return to menu (type: 0) | Show products (type: 1) | Add new product (type: 2) | \n Update existing product (type: 3) | Delete a product (type: 4)")
        
        products_menu_options_input = int(input("\n Select a menu option (0 | 1 | 2 | 3 | 4) - "))
        
        if products_menu_options_input == 0:
            clear()
            print("You have returned to the main menu \n")
        
        elif products_menu_options_input == 1:
            clear()
            print(f"Products available: {products}")
        
        elif products_menu_options_input == 2:
            clear()
            products = add_new_product(products)
        
        elif products_menu_options_input == 3:
            clear()
            edit_existing_product(products)
        
        elif products_menu_options_input == 4:
            clear()
            delete_product(products)
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    elif input_for_main_menu == 2:
        clear()
        print(f"\n Courier Menu")
        print("\n Options: \n Return to menu (type: 0) | View couriers available (type: 1) | Add new courier (type: 2) |\n Update existing courier (type: 3) | Remove existing courier (type: 4)")
        
        courier_menu_option_input = int(input("\n Select a menu option (0 | 1 | 2 | 3 | 4) - "))
        
        if courier_menu_option_input == 0:
            clear()
            print("You have returned to the main menu \n ")
        
        elif courier_menu_option_input == 1:
            clear()
            print(f"Couriers available: {couriers}")
        
        elif courier_menu_option_input == 2:
            clear()
            add_new_courier(couriers)
        
        elif courier_menu_option_input == 3:
            clear()
            edit_existing_courier(couriers)
        
        elif courier_menu_option_input == 4:
            clear()
            delete_courier(couriers)
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    elif input_for_main_menu == 3:
        clear()
        print("\n Order Menu")
        print("\n Options: \n Return to menu (type: 0) | View orders (type: 1) | Create new order (type: 2) |\n Update order status (type: 3) | Update Order (type: 4) | Delete order (type: 5)")
        
        order_menu_option_input = int(input("\n Select a menu option (0 | 1 | 2 | 3 | 4 | 5) - "))
        
        if order_menu_option_input == 0:
            clear()
            print("You have returned to the main menu \n")
        
        elif order_menu_option_input == 1:
            clear()
            show_orders(orders_list)
        
        elif order_menu_option_input == 2:
            clear()
            add_new_order(orders_list, couriers)
        
        elif order_menu_option_input == 3:
            clear()
            update_order_status(orders_list)
        
        elif order_menu_option_input == 4:
            clear()
            edit_existing_order(orders_list, couriers)
        
        elif order_menu_option_input == 5:
            clear()
            delete_order(orders_list)
    
    else:
        clear()
        print("That was not a valid option, please eneter a valid one.")