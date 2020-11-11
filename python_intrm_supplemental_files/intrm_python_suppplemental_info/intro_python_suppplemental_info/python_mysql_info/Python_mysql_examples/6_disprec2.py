import sys
import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="shree", db="shopping")
cursor=conn.cursor()
try:
    cursor.execute ("SELECT * from products")
    print ("Product ID\tProduct Name\tQuantity\tPrice")
    rows=cursor.fetchall()
    for row in rows:
        print ("%d\t\t%s\t\t%d\t\t%f"  %(row[0], row[1], row[2], row[3]))
except pymysql.Error:
    print ("Error in fetching rows")
    sys.exit(1)    
cursor.close()
conn.close()
