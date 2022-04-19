import sqlite3

def print_all(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    rows = cursor.execute("SELECT id, date,sender, message, placed FROM messages").fetchall()
    print(rows)
    connection.close()

def create_db(name):    
    conn = sqlite3.connect(name)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS messages (id INTEGER, date TEXT, sender TEXT, message TEXT, placed TEXT)")
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
    query = """ INSERT INTO messages VALUES ({0},'{1}','{2}','{3}','false')""".format(id_message ,message_date,sender_group,text_message)
    c.execute(query)
    conn.commit()
    print('TOTAL CHANGES WRITE MESSAGES : ',conn.total_changes)
    conn.close()


def get_new_id(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    last_id = cursor.execute("SELECT id FROM messages ORDER BY id DESC LIMIT 1").fetchall()
    connection.commit()
    connection.close()
    if last_id:
        return last_id[0][0] + 1
    else:
        return 1

def get_all_messages(db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    data = cursor.execute("SELECT id, date ,sender,message,placed FROM messages ORDER BY id DESC").fetchall()
    connection.close()
    return data