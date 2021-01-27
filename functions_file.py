import os

def clear():
    os.system( 'cls' )

def add_new_product(products):
    add_product = input("What product would you like to add? ").lower()
    products.append(add_product)
    return products

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