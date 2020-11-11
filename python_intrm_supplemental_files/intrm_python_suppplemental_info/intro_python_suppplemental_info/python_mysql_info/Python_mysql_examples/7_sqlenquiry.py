import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
cursor=conn.cursor()
p=int(input("Enter Product ID: "))
cursor.execute ("SELECT * from products where prod_id=%d" %p)
row=cursor.fetchone()
if row==None:
    print ("Sorry no Product found with ID %d" %p)
else:
    print ("Information of the product with ID %d is as follows:" %p)
    print ("Product ID: %d, Product Name: %s, Quantity: %d, Price: %f" %(row[0], row[1], row[2], row[3]))
cursor.close()
conn.close()


