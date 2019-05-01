#Handles fetching shortlinks & links from database
import psycopg2 as psql

def fetch_link(shortlink):
    '''Starts psql 'connection' instance and sets up a cursor.'''

    connection = psql.connect(user = "postgres", password = "qwerty123456", database = "initial_db")
    cur = connection.cursor()

    fetch_query = (""" SELECT * FROM short_link_table WHERE shortlink = %s; """)

    cur.execute(fetch_query, (shortlink,))
    retrieved = cur.fetchall()

    if retrieved is None:
        print("Link not Shortified")
        return 0
    else:
        cur.close()
        connection.commit()
        return(retrieved[0][2])

        
