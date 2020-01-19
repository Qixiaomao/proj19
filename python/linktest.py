import pandas  as pd 
import sqlite3 

conn = sqlite3.connect("humi.db")
sql = "SELECT * from  htdb;"
df = pd.read_sql(sql,conn)

print ("df")
print (df)