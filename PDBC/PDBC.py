import pymysql


mycon = pymysql.connect(host = "hipunl71603.ad.harman.com", user = "sa", passwd = "dell@123", database="python db", port=1433)

cur=mycon.cursor()

try:
    dbs = cur.execute("show databases")
    mycon.commit()
except:
    mycon.rollback()
finally:
    mycon.close()
