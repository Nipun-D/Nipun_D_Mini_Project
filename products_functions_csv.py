import os
import csv 

products_keys = ["name", "price"]

def clear():
    os.system( 'cls' )

def open_product_file(products_list):
    try:
        with open("products.csv", "r") as products_file:
            products_in_file = csv.DictReader(products_file)
            for row in products_in_file:
                products_list.append(row)
    except:
        print('Failed to open file')

def update_product_file(products_list):
    try:
        with open('products.csv', 'w', newline='') as products_file:
            products_in_file = csv.DictWriter(products_file, fieldnames = products_keys)
            products_in_file.writeheader()
            products_in_file.writerows(products_list)
    except Exception as e:
        print(f'Failed to open file {e}')

def show_products(products_list):
    clear()
    print("Product available:\n")
    for product in products_list:
        product_index = products_list.index(product)
        print(f"Product Number: {product_index}")
        for key, value in product.items():
            print(f"{key} : {value}")
        print("______________________________")

def add_new_product(products_list):
    new_product = {}
    new_product["Name"] = input("Product Name: ")
    new_product["Price"] = float(input("Product Price: "))
    products_list.append(new_product)

def edit_existing_product(products_list):
    print(f"Would you like to edit an existing product? \n")
    print("Options: \n Return to main menu (type 0) | Edit existing product (type 1) \n ")
    
    try:
        edit_options = int(input("Would you like to continue editing a product? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1:
        clear()  
        show_products(products_list)
        
        try:
            edit_input_index = int(input("Which item would you like to edit? \n please enter the product number - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if edit_input_index >= 0 and edit_input_index <= len(products_list):
            clear()
            print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
            
            new_product_name = input("Product name: ").lower()
            if new_product_name != "":
                products_list[edit_input_index]["Name"] = new_product_name
            
            new_product_price = input("Product price: ")
            if new_product_price != "":
                products_list[edit_input_index]["Price"] = float(new_product_price)
        else:
            clear()
            print("That was an invalid product number")
    else:
        clear()
        print("That was an invalid input")

def delete_product(products_list):
    print(f"Would you like to delete a product? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing product (type 1) \n ")
    
    try:
        delete_options = int(input("Would you like to continue removing a product? "))
    except:
        clear()
        print("That was an invalid option")
        continue
    
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        clear()
        show_products(products_list)
        
        try:
            delete_product_index = int(input("Please enter the product number of the product you wish to delete - "))
        except:
            clear()
            print("That was an invalid option")
            continue
        
        if delete_product_index >= 0 and delete_product_index <= len(products_list):
            del products_list[delete_product_index]
        else:
            clear()
            print("Product {delete_product_index} does not exist.")
    else:
        clear()
        print("That was an invalid input")
