import psycopg2

#c6nnect to postgres
conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=1997")
cur = conn.cursor()

with open('/home/sunbee/batchpro/source/users_w_postal_code.csv','r') as f:
    next(f)
    cur.copy_from(f,'latihan_users',sep=',',columns=('email','name','phone','postal_code'))
conn.commit()