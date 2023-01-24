import psycopg2
import pandas as pds
import pandas.io.sql as sqlio

#c6nnect to postgres
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=1997")
    print("connection success")
except:
    print("An exception occurred")


#menggunakan cursor

cur = conn.cursor()
cur.execute("Select * from bptn.category_db")

#menampilkan hasil
all = cur.fetchall()
one = cur.fetchone()
conn.commit()

for record in all:
    print(str(record[0]) +"-"+ record[1])