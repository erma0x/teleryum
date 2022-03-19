import sqlite3

connection = sqlite3.connect("aquarium.db")

print(connection.total_changes)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS fish (name TEXT, species TEXT, tank_number INTEGER)")
cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

released_fish_name = "Sammy"
rows2 =  cursor.execute(
    "DELETE FROM fish WHERE name = ?",
    (released_fish_name,))

rows = cursor.execute("SELECT name, species, tank_number FROM fish").fetchall()
print(rows)

connection.close()


connection = sqlite3.connect(NAME_DB)
cursor = connection.cursor()

cursor.execute("INSERT INTO messages VALUES (1,'2022-03-02 04:40:00+00:00','Fat Pig Signals','Sell 24432 BTCUSDT')")
cursor.execute("INSERT INTO messages VALUES (2,'2022-03-02 04:41:01+00:00','AltSignals','Buy 24433 BTCUSDT')")
cursor.execute("INSERT INTO messages VALUES (3,'2022-03-02 04:42:02+00:00','Fat Pig Signals','Buy 24435 BTCUSDT')")
cursor.execute("INSERT INTO messages VALUES (4,'2022-03-02 04:43:03+00:00','AltSignals','Sell 24439 BTCUSDT')")
cursor.execute("INSERT INTO messages VALUES (5,'2022-03-02 04:44:04+00:00','Fat Pig Signals','#OG Buy 792-770 Sell 805-820-878-1100 StopLoss 670 By (@SN_crypto) 2022-03-02 04:41:12+00:00 ')")
connection.commit()
connection.close()