#Handles uploading shortlinks to database
import psycopg2 as psql

def upload_link(shortlink, fulllink):
    '''Starts psql 'connection' instance and sets up a cursor'''

    connection = psql.connect(user = "postgres", password = "qwerty123456", database = "initial_db")
    cur = connection.cursor()

    duplication_query = (""" SELECT * FROM short_link_table WHERE shortlink = %s; """)
    insertion_query = ("""
                INSERT INTO short_link_table(shortlink, fulllink, creation_date, updation_date)
                SELECT %s, %s, current_timestamp, current_timestamp
                WHERE
                NOT EXISTS ( SELECT shortlink FROM short_link_table WHERE shortlink = %s );
                    """) #Inserts value only if it is absent

    cur.execute(duplication_query,(shortlink,))
    retrieved = cur.fetchall()

    if len(retrieved) > 0:
        db_fulllink = retrieved[0][2] #Stores the fulllink corresponding to the mathches

        if db_fulllink == fulllink:
            cur.close()
            connection.commit()
            return True #Fullink already exists
        else:
            cur.close()
            connection.commit()
            return False #Shortlink collision
        
    else:
        cur.execute( insertion_query, (shortlink, fulllink, shortlink,) )
        cur.close()
        connection.commit()
        return True
        
