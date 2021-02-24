import sys
import os
import pymysql
from products_functions_sql import *
from couriers_functions_sql import *
from orders_functions_sql import *

print('\nWelcome to the app!')

my_db = pymysql.connect(
    "localhost",
    "root",
    "password",
    "mini_project"
)

def clear():
    os.system( 'cls' )

while True:
    
    print("\n~~~~~~~~~~~~~")
    print("| Main Menu |")
    print("~~~~~~~~~~~~~")
    print('\nOptions: \nSave & close app (type: 0) | Products Menu (type: 1) | Couriers Menu (type: 2) | Orders Menu (type: 3)')
    try:
        input_for_main_menu = int(input("\nSelect a menu option (0 | 1 | 2 | 3) - "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if input_for_main_menu == 0:
        clear()
        my_db.close()
        print("Thank you for using the app")
        sys.exit(0)
    
    elif input_for_main_menu == 1:
        clear()
        print("\n~~~~~~~~~~~~~~~~~")
        print("| Products Menu |")
        print("~~~~~~~~~~~~~~~~~")
        print("\nOptions: \nReturn to menu (type: 0) | Show products (type: 1) | Add new product (type: 2) | \n Update existing product (type: 3) | Delete a product (type: 4)")
        try:
            products_menu_options_input = int(input("\nSelect a menu option (0 | 1 | 2 | 3 | 4) - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if products_menu_options_input == 0:
            clear()
            print("You have returned to the main menu \n")
        
        elif products_menu_options_input == 1:
            clear()
            show_products(my_db)
        
        elif products_menu_options_input == 2:
            clear()
            add_new_product(my_db)
        
        elif products_menu_options_input == 3:
            clear()
            edit_existing_product(my_db)
        
        elif products_menu_options_input == 4:
            clear()
            delete_product(my_db)
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    elif input_for_main_menu == 2:
        clear()
        print("\n~~~~~~~~~~~~~~~~")
        print("| Courier Menu |")
        print("~~~~~~~~~~~~~~~~")
        print("Options: \nReturn to menu (type: 0) | View couriers available (type: 1) | Add new courier (type: 2) |\n Update existing courier (type: 3) | Remove existing courier (type: 4)")
        try:
            courier_menu_option_input = int(input("\nSelect a menu option (0 | 1 | 2 | 3 | 4) - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if courier_menu_option_input == 0:
            clear()
            print("You have returned to the main menu \n ")
        
        elif courier_menu_option_input == 1:
            clear()
            show_couriers(my_db)
        
        elif courier_menu_option_input == 2:
            clear()
            add_new_courier(my_db)
        
        elif courier_menu_option_input == 3:
            clear()
            edit_existing_courier(my_db)
        
        elif courier_menu_option_input == 4:
            clear()
            delete_courier(my_db)
        
        else:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    elif input_for_main_menu == 3:
        clear()
        print("\n~~~~~~~~~~~~~~")
        print("| Order Menu |")
        print("~~~~~~~~~~~~~~")
        print("\nOptions: \nReturn to menu (type: 0) | View orders (type: 1) | Create new order (type: 2) |\n Update order status (type: 3) | Update Order (type: 4) | Delete order (type: 5)")
        
        try:
            order_menu_option_input = int(input("\nSelect a menu option (0 | 1 | 2 | 3 | 4 | 5) - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if order_menu_option_input == 0:
            clear()
            print("You have returned to the main menu \n")
        
        elif order_menu_option_input == 1:
            clear()
            show_orders(my_db)
        
        elif order_menu_option_input == 2:
            clear()
            add_new_order(my_db)
        
        elif order_menu_option_input == 3:
            clear()
            update_order_status(my_db)
        
        elif order_menu_option_input == 4:
            clear()
            edit_existing_order(my_db)
        
        elif order_menu_option_input == 5:
            clear()
            delete_order(my_db)
    
    else:
        clear()
        print("That was not a valid option, please eneter a valid one.")