import sys
import pymysql
try:
    conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
except pymysql.Error:
    print ("Error in establishing connection")
    sys.exit(1)    
cursor=conn.cursor()
try:
    cursor.execute("""
    INSERT INTO products (prod_id, prod_name, quantity, price)
    VALUES (101, 'Camera', 100, 15)
    """)
    conn.commit()
    print('One row inserted into the products table')
except:
    conn.rollback()
cursor.close()
conn.close()
 
