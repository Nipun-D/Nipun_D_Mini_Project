import os

#TODO -
#try and except errors
# -Incorrect input/input type(Str/int)

def clear():
    os.system( 'cls' )

def show_couriers(my_db):
    clear()
    id = "ID"
    name = "Name"
    number = "Courier Number"
    print("Couiers available:\n")
    print(id.center(10), name.center(20), number.center(20))
    print("---------------------------------------------------")
    mycursor = my_db.cursor()
    sql = "SELECT * FROM couriers"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()  
    for row in myresult:
        row0 = str(row[0]).center(10)
        row1 = str(row[1]).center(20)
        row2 = str(row[2]).center(20)
        print(row0, row1, row2)
    mycursor.close()

def add_new_courier(my_db):
    clear()
    mycursor = my_db.cursor()
    
    courier_name = input("Courier: ").title().strip()
    
    while True:
        try:
            courier_number = int(input("Courier Number: "))
            break
        except:
            print("That was an invalid input, please eneter a valid one.")
    
    reset_auto_increment = "ALTER TABLE couriers AUTO_INCREMENT = 1"
    mycursor.execute(reset_auto_increment)
    
    sql = "INSERT INTO couriers (courier, courier_phone_number) VALUES (%s, %s)"
    mycursor.execute(sql, (courier_name, courier_number))
    my_db.commit()
    mycursor.close()

def edit_existing_courier(my_db):
    mycursor = my_db.cursor()
    
    while True:
        try:
            print(f"Would you like to edit an existing courier? \n")
            print("""Options: 
                \nReturn to main menu (type 0) | Edit existing courier (type 1) \n """)
            edit_options = int(input("Would you like to continue editing an existing courier? "))
            break
        except:
            clear()
            print("That was not a valid option, please eneter a valid one.")
    
    if edit_options == 0:
        clear()
        return None
    elif edit_options == 1: 
        clear()  
        
        while True:
            try:
                show_couriers(my_db)
                edit_input_index = int(input("\nWhich courier would you like to edit? \nPlease enter the courier ID - "))
                sql = "SELECT couriers_id FROM couriers WHERE couriers_id = %s"
                mycursor.execute(sql, edit_input_index)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was not a valid option, please eneter a valid one.")
        
        print("If you are happy and do NOT wish to update this information, then please press ENTER to skip. ")
        
        clear()
        new_courier_name = input("Courier name: ").title().strip()
        if new_courier_name != "":
            sql = "UPDATE couriers SET courier = %s WHERE couriers_id = %s"
            mycursor.execute(sql, (new_courier_name, edit_input_index)) 
            my_db.commit()  
        
        new_courier_number = input("Courier number : ")
        if new_courier_number != "":
            sql = "UPDATE couriers SET courier_phone_number = %s WHERE couriers_id = %s"
            mycursor.execute(sql, (new_courier_number, edit_input_index))
            my_db.commit()
        
        mycursor.close()
    else:
        clear()
        print("That was an invalid input")

def delete_courier(my_db):
    clear()
    while True:
        try:
            clear()
            print(f"Would you like to remove a courier? \n")
            print("""Options: 
                \nReturn to main menu (type 0) | Remove existing courier (type 1) \n """)
            delete_options = int(input("Would you like to continue removing a courier? "))
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
                show_couriers(my_db)
                delete_courier_index = int(input("Please enter the courier ID of the courier you wish to remove - "))
                sql = "SELECT couriers_id FROM couriers WHERE couriers_id = %s"
                mycursor.execute(sql, delete_courier_index)
                result = mycursor.fetchone()
                if result != None:
                    break
                else:
                    print("That was an invalid option.\n")
            except:
                clear()
                print("That was an invalid option")
        
        mycursor = my_db.cursor()
        sql = "DELETE FROM couriers WHERE couriers_id = %s"
        mycursor.execute(sql, delete_courier_index)
        my_db.commit()
        mycursor.close()
    else:
        clear()
        print("That was an invalid input")