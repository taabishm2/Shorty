import psycopg2 as psql

def sql_insert(shortlink,fulllink):
    '''Carry out find or create. If entry not found in DB, insert. Otherwise do nothing. Returns index of entry'''

    query = ("""
                INSERT INTO short_link_table(shortlink, fulllink, creation_date, updation_date)
                SELECT %s, %s, current_timestamp, current_timestamp
                WHERE
                NOT EXISTS (
                    SELECT shortlink FROM short_link_table WHERE shortlink = %s
                );
            """) #Inserts value only if it is absent

    connection = psql.connect(user = "postgres", password = "qwerty123456", database = "initial_db")
    cur = connection.cursor()

    cur.execute( query, (shortlink, fulllink, shortlink,) )

    cur.close()
    connection.commit()
    
