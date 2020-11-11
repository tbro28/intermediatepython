import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
cursor=conn.cursor()
cursor.execute("""
INSERT INTO products (prod_id, prod_name, quantity, price)
VALUES (101, 'Camera', 100, 15)
""")
print('One row inserted into the products table')
cursor.close()
conn.commit()
conn.close()
