import csv
import os
import pymysql
from couriers_functions_sql import show_couriers
from products_functions_sql import show_products

#TODO -
#try and except errors 
# -Incorrect input/input type(Str/int)

def clear():
    os.system( 'cls' )

def show_orders(my_db):
    clear()
    
    id = "ID"
    name = "Customer Name"
    address = "Customer Address"
    phone = "Customer Phone"
    courier = "Courier"
    status = "Status"
    items = "Items"
    
    print("Current Orders:\n")
    print(id.center(10), name.center(20), address.center(30), phone.center(20), status.center(20), courier.center(20), items.center(20))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
    mycursor = my_db.cursor()
    sql1 = """SELECT o.order_id, o.customer_name, o.customer_address, o.customer_phone, o.status, c.courier AS couriers_id, GROUP_CONCAT(p.product SEPARATOR ', ') 
        FROM orders o 
        INNER JOIN couriers c ON o.courier = c.couriers_id       
        INNER JOIN orders_products op ON op.order_id = o.order_id
        JOIN products p ON p.product_id = op.product_id
        GROUP BY op.order_id"""
    
    mycursor.execute(sql1)
    myresult = mycursor.fetchall()
    
    for row in myresult:
        row0 = str(row[0]).center(10)
        row1 = str(row[1]).center(20)
        row2 = str(row[2]).center(30)
        row3 = str(row[3]).center(20)
        row4 = str(row[4]).center(20)
        row5 = str(row[5]).center(20)
        row6 = str(row[6]).center(20)
        
        print(row0, row1, row2, row3, row4, row5, row6, "\n")
    mycursor.close()

def add_new_order(my_db):
    clear()
    mycursor = my_db.cursor()
    
    #Resets auto increment
    reset_auto_increment = "ALTER TABLE orders AUTO_INCREMENT = 1" 
    mycursor.execute(reset_auto_increment)
    
    customer_name = input("Customer name: ").strip().title()
    customer_address = input("Customer address: ").strip().title()
    customer_phone = input("Customer phone: ").strip()
    while True:
        try:
            show_couriers(my_db)
            courier = int(input("\nSelect a courier from above.\nCourier: "))
            break
        except:
            print("That was an invalid input.")
    
    
    sql = """INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status) VALUES (%s, %s, %s, %s, 'preparing')"""
    mycursor.execute(sql, (customer_name, customer_address, customer_phone, courier))
    my_db.commit()
    
    add_products_to_order(my_db)
    
    mycursor.close()

def add_products_to_order(my_db):
    mycursor = my_db.cursor()
    while True:
        show_products(my_db)
        print("\nAdd in the product ID of the product you wish to add to the order. Press 0 if you wish to finish adding products.\n")
        item = int(input("Product ID - "))
        if item == 0:
            break
        else:
            sql = """INSERT INTO orders_products (order_id, product_id) VALUES (LAST_INSERT_ID(), %s)"""
            mycursor.execute(sql, item)
    my_db.commit()
    mycursor.close()

def update_order_status(my_db):
    clear()
    mycursor = my_db.cursor()
    
    while True:
        try:
            print("Would you like to update the status of an order?\n")
            print("""Options: 
                \nCancel (type 0) | Edit order status (type 1) \n """)
            status_order = int(input("Would you still like to update an order status? "))
            break
        except:
            clear()
            print("That was an invalid option")
    
    if status_order == 0:
        clear()
        return None
    elif status_order == 1:
        clear()
        
        while True:
            try:
                show_orders(my_db)
                order_status_order_number = int(input("Which order would you like to change the status of? "))
                sql = "SELECT order_id FROM orders WHERE order_id = %s"
                mycursor.execute(sql, order_status_order_number)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid option")
        
        while True:
            print("Please enter: Preparing - P | Delivered - D")
            new_order_status = input("Order Status: ").lower()[0].strip()
            if new_order_status == "p":
                status_change = "preparing"
                sql = "UPDATE orders SET status = %s WHERE order_id = %s"
                mycursor.execute(sql, (status_change, order_status_order_number)) 
                my_db.commit()
                break
            elif new_order_status == "d":
                status_change = "delivered"
                sql = "UPDATE orders SET status = %s WHERE order_id = %s"
                mycursor.execute(sql, (status_change, order_status_order_number)) 
                my_db.commit()
                break
            else:
                print("That was an invalid input")
        
        mycursor.close()
    else:
        clear()
        print("That was an invalid input")

def edit_existing_order(my_db):
    clear()
    mycursor = my_db.cursor()
    while True:
        try:
            print("Would you like to edit an order?")
            print("""\nOptions: 
                \nReturn to main menu (type 0) | Edit existing order (type 1) \n """)
            edit_options = int(input("Would you like to continue editing an existing order? "))
            break
        except:
            clear()
            print("That was an invalid option")
    
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1:
        clear()
        
        while True:
            try:
                show_orders(my_db)
                edit_input_index = int(input("Which order would you like to edit? \nPlease enter the order number - \n"))
                sql = "SELECT order_id FROM orders WHERE order_id = %s"
                mycursor.execute(sql, edit_input_index)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid input")
        
        clear()
        print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
        new_customer_name = input("Customer Name: ").title().strip()
        if new_customer_name != "":
            sql = "UPDATE orders SET customer_name = %s WHERE order_id = %s"
            mycursor.execute(sql, (new_customer_name, edit_input_index)) 
            my_db.commit()
        
        clear()
        print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
        new_customer_address = input("Customer address: ").title().strip()
        if new_customer_address != "":
            sql = "UPDATE orders SET customer_address = %s WHERE order_id = %s"
            mycursor.execute(sql, (new_customer_address, edit_input_index)) 
            my_db.commit()
        
        clear()
        print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
        new_customer_phone = input("Customer phone: ").strip()
        if new_customer_phone != "":
            sql = "UPDATE orders SET customer_address = %s WHERE order_id = %s"
            mycursor.execute(sql, (new_customer_phone, edit_input_index)) 
            my_db.commit()
        
        clear()
        while True:
            try:
                show_couriers(my_db)
                print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
                new_courier = int(input("Courier: "))
                break
            except:
                print("That was an invalid input.")
        new_courier = str(new_courier)
        if new_courier != "":
            sql = "UPDATE orders SET courier = %s WHERE order_id = %s"
            mycursor.execute(sql, (int(new_courier), edit_input_index)) 
            my_db.commit()
        
        while True:
            try:
                clear()
                print("""Would you like to change the products in this order? \n(NOTE: If you wish to edit the products in this please re-enter the products you wish to keep)
                    \nOptions: 
                    \nFinish editing order and return to main menu (type 0) | Edit products in this order (type 1) \n  """)
                product_change_input = int(input("Would you like to continue editing the products in this order? "))
                break
            except:
                print("That was an invalid input.")
        
        if product_change_input == 0:
            return None
        if product_change_input == 1:
            sql1 = "DELETE FROM orders_products WHERE order_id = %s"
            mycursor.execute(sql1, edit_input_index)
            while True:
                show_products(my_db)
                print("\nAdd in the product ID of the product you wish to add to the order. Press 0 if you wish to finish adding products.\n")
                item = int(input("Product ID - "))
                if item == 0:
                    break
                else:
                    sql2 = """INSERT INTO orders_products (order_id, product_id) VALUES (%s, %s)"""
                    mycursor.execute(sql2, (edit_input_index, item))
            my_db.commit()
        else:
            print("That was and invalid input.")
        mycursor.close()
    else:
        clear()
        print("That was and invalid input")

def delete_order(my_db):
    clear()
    while True:
        try:
            clear()
            print("Would you like to delete an order?")
            print("""Options: 
                \nReturn to main menu (type 0) | Remove existing order (type 1) \n """)
            delete_options = int(input("Would you like to continue removing an order? "))
            break
        except:
            clear()
            print("That was an invalid option")
    
    if delete_options == 0:
        clear()
        return None
    elif delete_options == 1:
        clear()
        while True:
            try:
                show_orders(my_db)
                delete_order_index = int(input("Please enter the order number of the order you wish to delete - "))
                sql = "SELECT order_id FROM orders WHERE order_id = %s"
                mycursor.execute(sql, delete_order_index)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid option")
        
        mycursor = my_db.cursor()
        sql2 = "DELETE FROM orders_products WHERE order_id = %s"
        mycursor.execute(sql2, delete_order_index)
        sql1 = "DELETE FROM orders WHERE order_id = %s"
        mycursor.execute(sql1, delete_order_index)
        my_db.commit()
        mycursor.close()
    else:
        clear()
        print("That was an invalid input.")