import psycopg2 as psql

def check_duplication(shortlink,fulllink):
    '''Checks if same shortlink exists for a different long link. Return value 0 indicates fulllink already present in Db.'''

    query_short = (""" SELECT * FROM short_link_table WHERE shortlink = %s; """)

    connection = psql.connect(user = "postgres", password = "qwerty123456", database = "initial_db")
    cur = connection.cursor()

    cur.execute(query_short,(shortlink,))
    retrieved = cur.fetchall()

    if len(retrieved) > 0:
        db_fulllink = retrieved[0][2] #Stores the fulllink corresponding to the mathches

        if db_fulllink == fulllink: #Fullink already exists
            return 0
        else:
            return 1 #Shortlink collision

    else:
        return -1 #Current short or long links don't exist in Db

    cur.close()
    connection.commit()

    
