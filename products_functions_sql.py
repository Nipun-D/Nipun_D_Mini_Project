import os

#TODO -
#try and except errors
# -Incorrect input/input type(Str/int)

def clear():
    os.system( 'cls' )

def show_products(my_db):
    clear()
    price = "Price (£)"
    id = "ID"
    product = "Product"
    print("Product available:\n")
    print(id.center(10), product.center(20), price.center(20))
    print("--------------------------------------------------------------")
    mycursor = my_db.cursor()
    sql = "SELECT * FROM products"
    mycursor.execute(sql)
    myresult = mycursor.fetchall() 
    for row in myresult:
        row0 = str(row[0]).center(10)
        row1 = str(row[1]).center(20)
        row2 = str(row[2]).center(20)
        print(row0, row1, row2)
    mycursor.close()

def add_new_product(my_db):
    clear()
    mycursor = my_db.cursor()
    
    product_name = input("Product: ").title().strip()
    
    while True:
        try:
            product_price = float(input("Price: "))
            break
        except:
            print("Invalid price value was inserted.\n")
    
    reset_auto_increment = "ALTER TABLE products AUTO_INCREMENT = 1"
    mycursor.execute(reset_auto_increment)
    
    sql = "INSERT INTO products (product, price) VALUES (%s, %s)"
    mycursor.execute(sql, (product_name, product_price))
    my_db.commit()
    mycursor.close()

def edit_existing_product(my_db):
    mycursor = my_db.cursor()
    
    while True:
        try:
            print(f"Would you like to edit an existing product?")
            print("""\nOptions: 
                \nReturn to main menu (type 0) | Edit existing product (type 1) \n """)
            edit_options = int(input("Would you like to continue editing a product? "))
            break
        except:
            clear()
            print("That was an invalid option. \n")
    
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1:
        clear()  
        
        while True:
            try:
                show_products(my_db)
                edit_input_index = int(input("\nWhich product would you like to edit? \nplease enter the product ID - "))
                sql = "SELECT product_id FROM products WHERE product_id = %s"
                mycursor.execute(sql, edit_input_index)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid option.\n")
        
        clear()
        print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
        
        new_product_name = input("Product name: ").title().strip()
        if new_product_name != "":
            sql = "UPDATE products SET product = %s WHERE product_id = %s"
            mycursor.execute(sql, (new_product_name, edit_input_index)) 
            my_db.commit()  
        
        change_new_product_price = ""
        while True:
            try:
                new_product_price = float(input("Product price: "))
                change_new_product_price = str(new_product_price)
                break
            except:
                clear()
                print("That was an invalid input.\n")
            finally:
                if change_new_product_price != "":
                    sql = "UPDATE products SET price = %s WHERE product_id = %s"
                    mycursor.execute(sql, (float(new_product_price), edit_input_index))
                    my_db.commit()
                    break
                break
        
        mycursor.close()
    else:
        clear()
        print("That was an invalid input")

def delete_product(my_db):
    mycursor = my_db.cursor()
    while True:
        try:
            clear()
            print("\nWould you like to delete a product?")
            print("""\nOptions: 
                \nReturn to main menu (type 0) | Remove existing product (type 1) \n """)
            delete_options = int(input("Would you like to continue removing a product? "))
            break
        except:
            print("That was an invalid input.\n")
    
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        clear()
        while True:
            try:
                show_products(my_db)
                delete_product_input = int(input("\nPlease enter the product ID of the product you wish to remove - "))
                sql = "SELECT product_id FROM products WHERE product_id = %s"
                mycursor.execute(sql, delete_product_input)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid input.\n")
        
        sql = "DELETE FROM orders_products WHERE product_id = %s"
        mycursor.execute(sql, delete_product_input)
        sql2 = "DELETE FROM products WHERE product_id = %s"
        mycursor.execute(sql2, delete_product_input)
        my_db.commit()
        mycursor.close()
    else:
        clear()
        print("That was an invalid input")