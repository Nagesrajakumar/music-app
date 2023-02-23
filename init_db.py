import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

# cur = connection.cursor()

# cur.execute("INSERT INTO songs (title, artist, album) VALUES (?, ?)",
#             ('Beast Mode', 'Anirudh', 'Beast')
#             )

# cur.execute("INSERT INTO songs (title, artist, album) VALUES (?, ?)",
#             ('Take You', 'Justin Bieber', 'Believe')
#             )

# connection.commit()
# connection.close()