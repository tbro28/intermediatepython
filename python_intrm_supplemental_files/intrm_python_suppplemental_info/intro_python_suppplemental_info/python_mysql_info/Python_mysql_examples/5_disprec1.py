import sys
import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
cursor=conn.cursor()
try:
    cursor.execute ("SELECT * from products")
    print ("Product ID\tProduct Name\tQuantity\tPrice")
    while(1):
        row=cursor.fetchone()
        if row==None:
            break
        print ("%d\t\t%s\t\t%d\t\t%f"  %(row[0], row[1], row[2], row[3]))
except pymysql.Error:
    print ("Error in fetching rows")
    sys.exit(1)    
cursor.close()
conn.close()
