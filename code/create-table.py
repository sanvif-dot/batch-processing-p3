import psycopg2

#c6nnect to postgres
conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=1997")
cur = conn.cursor()

#create table
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

cur.execute("INSERT INTO latihan_users VALUES (%s, %s, %s, %s, %s)", (1, 'hello@dataquest.io', 'Some Name', '621234413', '12343'))
conn.commit()
print("Create Table Succes")
