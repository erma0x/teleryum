import sqlite3
import json

messages = {
1: 
{
'sender':'Crypto Signals Free',
'text':"""
#OG 
Buy 792-770
Sell 805-820-878-1100
StopLoss 670
By (@SN_crypto)
2022-02-28 04:13:09+00:00
"""
},
2: 
{
'sender':'Crypto Signals Free',
'text':"""
#BTC 
Buy 792-770
Sell 805-820-878-1100
StopLoss 670
By (@SN_crypto)
2022-02-28 04:16:19+00:00
"""
}

}

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_db():    
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (id_message INTEGER, data TEXT, sender TEXT,text TEXT)")
    conn.close() 

def show_tables():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print('MY TABLES ',c.fetchall())
    conn.close()

def show_columns(table_name):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info({});".format(table_name))
    print('MY COLUMNS ',c.fetchall())
    print('TOTAL CHANGES ',conn.total_changes)

    conn.close()

def show_all():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    query= "SELECT * FROM messages;"
    print('MY show_all ',c.fetchall())
    c.execute(query)
    all_rows = c.fetchall()
    for row in all_rows:
        # row[0] returns the first column in the query (name), row[1] returns email column.
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    print('TOTAL CHANGES ',conn.total_changes)
    conn.close()


def get_last_id_message():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT id_message FROM messages ORDER BY id_message DESC;")
    last_id_message = c.fetchall()
    print('GET LAST ID: ',last_id_message)
    print('TOTAL CHANGES ',conn.total_changes)
    conn.close()
    return(last_id_message)
    

def write_message(id_message, message_date,sender_group,text_message):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    query = """ INSERT INTO messages VALUES ('{0}','{1}','{2}','{3}')""".format(id_message ,message_date,sender_group,text_message)
    #query="INSERT INTO messages (sender, text) VALUES ({0}, {1});".format(sender_group,text_message)
    task = ()
    rows = c.execute(query,task).fetchall()
    print('ROWS ',rows)
    print('TOTAL CHANGES WRITE MESSAGES : ',conn.total_changes)
    conn.close()

# da verificare che il db e' connesso
# inserire e riprendere i dati in un formato consono
# mandarlo il live e vedere se li cattura

# create_db()

# write_message(1,'2022-03-02 04:40:00+00:00',sender_group='Fat Pig Signals',text_message='Sell 24432 BTCUSDT')
# write_message(2,'2022-03-02 04:40:01+00:00',sender_group='AltSignals',text_message='Buy 24432 ETHUSDT')

# #show_tables()
# #show_columns('messages')
# #show_all()

# #last_id = get_last_id_message()

# conn = sqlite3.connect('test.db')
# c = conn.cursor()
# rows = c.execute("SELECT * FROM messages").fetchall()
# print(rows)


# conn.close()


import sqlite3


def print_all(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    rows = cursor.execute("SELECT id, date,sender, message FROM messages").fetchall()
    print(rows)
    connection.close()

def create_db(name):    
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER, date TEXT, sender TEXT, message TEXT )")
    conn.close() 

def print_changes(db):
    conn = sqlite3.connect(db)
    print("TOTAL CHANGES: ",conn.total_changes)
    conn.close() 

def delete_id(id_,db):
    old_id = id_
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM messages WHERE id = ?",(old_id,))
    connection.commit()
    connection.close()

def write_message(id_message, message_date,sender_group,text_message,NAME_DB):
    conn = sqlite3.connect(NAME_DB)
    c = conn.cursor()
    query = """ INSERT INTO messages VALUES ({0},'{1}','{2}','{3}')""".format(id_message ,message_date,sender_group,text_message)
    #query="INSERT INTO messages (sender, text) VALUES ({0}, {1});".format(sender_group,text_message)
    #task=(id_message, message_date,sender_group,text_message)
    c.execute(query)
    conn.commit()
    print('TOTAL CHANGES WRITE MESSAGES : ',conn.total_changes)
    conn.close()

def get_last_id_message(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    last_id = cursor.execute("SELECT id FROM messages ORDER BY id DESC LIMIT 1").fetchall()
    connection.commit()
    connection.close()
    return last_id[0][0]

NAME_DB = "teleryum.db"


create_db(NAME_DB)

print_changes(NAME_DB)

delete_id(1,NAME_DB)

write_message(5,'2022-03-02 04:44:04+00:00','Fat Pig Signals','#OG Buy 792-770',NAME_DB)
write_message(6,'2022-03-02 04:44:04+00:00','Fat Pig Signals','#OG Buy 792-770',NAME_DB)
write_message(7,'2022-03-02 04:44:04+00:00','Fat Pig Signals','#OG Buy 792-770',NAME_DB)

print_all(NAME_DB)
last_id =get_last_id_message(NAME_DB)
print(int(last_id))