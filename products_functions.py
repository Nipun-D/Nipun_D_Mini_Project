import os

def clear():
    os.system( 'cls' )

def open_product_file(products):
    try:
        with open("products.txt",'r') as products_file:
            products_in_file = products_file.readlines()
            for product in products_in_file:
                products.append(product.rstrip())
    except:
        print('Failed to open file')

def update_product_file(products):
    try:
        with open("products.txt",'w') as products_file:
            for product in products:
                products_file.write(product + '\n')
    except:
        print('Failed to open file')

def add_new_product(products):
    add_product = input("What product would you like to add? ").lower()
    products.append(add_product)
    return products

def edit_existing_product(products):
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
        if edit_input_index >= 0 and edit_input_index <= len(products):
            edit_input_product = input("Enter the new product name: ").lower()
            products[edit_input_index-1] = edit_input_product
        else:
            clear()
            print("That was an invalid product number")
    else:
        clear()
        print("That was an invalid input")

def delete_product(products):
    print(f"Products available to remove: {products} \n Would you like to delete a product? \n")
    print("Options: \n Return to main menu (type 0) | Remove existing product (type 1) \n ")
    delete_options = int(input("Would you like to continue removing a product? "))
    if delete_options == 0:
        clear()
        return None
    elif delete_options ==1:
        delete_input_product = input("Which product would you like to remove? ").lower()
        if delete_input_product in products:
            products.remove(delete_input_product)
        else:
            clear()
            print(f"The product {delete_input_product} is not in the products list")
    else:
        clear()
        print("That was an invalid input")
