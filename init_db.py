import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO songs (title, artist) VALUES (?, ?)",
#             ('Beast Mode', 'Anirudh')
#             )

# cur.execute("INSERT INTO songs (title, artist) VALUES (?, ?)",
#             ('Take You', 'Justin Bieber')
#             )

# connection.commit()
# connection.close()