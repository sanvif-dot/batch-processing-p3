import psycopg2
import csv

#c6nnect to postgres
conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=1997")
cur = conn.cursor()

cur.execute("""
                CREATE TABLE IF NOT EXISTS latihan_users(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postal_code text
                )
    """
    )

with open('/home/sunbee/batchpro/source/users_w_postal_code.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader) #skip header
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_users VALUES ( default, %s, %s, %s,%s) ON CONFLICT DO NOTHING", row)
    
conn.commit()
#cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s,%s)", (1, 'hello@dataquest.io', 'Some Name','621234413', '12343'))
#conn.commit()
#print("Create Table Success")