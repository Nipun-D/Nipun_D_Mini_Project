import pymysql

my_db = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "mini_project",
)

# SELECT orders.order_id, \
    # orders.customer_name, \
    # orders.customer_address, \
    # orders.customer_phone, \
    # orders.status, \
    # couriers.courier AS couriers_id, \
    # (SELECT GROUP_CONCAT(op.product_id) FROM orders_products op WHERE op.order_id = orders.order_id) AS product_ids \
    # (SELECT GROUP_CONCAT(p.product) FROM products p WHERE p.product_id = op.product_id) AS product_names \
    # FROM orders \
    # JOIN couriers ON orders.courier = couriers.couriers_id \
    # JOIN orders_products on orders.order_id = orders_products.order_id \
    # JOIN products on products.product_id = orders_products.product_id \
    # GROUP BY orders.order_id


# def get_products_from_order(my_db):
#     mycursor = my_db.cursor()
#     sql = "SELECT items FROM orders WHERE order_id = 2"
#     mycursor.execute(sql)
#     myresult = mycursor.fetchall()
#     list_product_id = []
#     for row in myresult:
#         row0 = row[0]
#         for character in row0:
#             if character.isdigit():
#                 list_product_id.append(int(character))


def show_products_in_order(my_db, order_id):
    mycursor = my_db.cursor()
    
    sql = "SELECT items FROM orders WHERE order_id = 2"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    list_product_id = []
    for row in myresult:
        row0 = row[0]
        for character in row0:
            if character.isdigit():
                list_product_id.append(int(character))
    print(list_product_id)
    
    list_product = ""
    for i in list_product_id:
        sql = "SELECT product FROM products WHERE product_id = %s"
        mycursor.execute(sql, str(i))
        products_in_order = mycursor.fetchall()
        for product in products_in_order:
            product = str(product)
            #list_product.append(str(product))
            list_product = list_product + product
    return list_product.replace(",", "").replace("(", "").replace(")", "")
    mycursor.close()

items = show_products_in_order(my_db, 2)
print(items)
