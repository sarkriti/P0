import sqlite3
from person import Person

conn = sqlite3.connect('people.db')
mycursor = conn.cursor()

p1 = Person('judy','syuejw','lzy6253','working on homework','678tyw')
#p2 = Person('hubert','jwoiaf','lzy6253','working on homework','097hsgj')

# Create a table

# mycursor.execute(
#     """CREATE TABLE people (
#         name text,
#         username text,
#         password text,
#         status text,
#         session text
#     )
# """)

mycursor.execute("INSERT INTO people VALUES (:name,:username,:password,:status,:session)",{'name': p1.name,'username':p1.username,'password': p1.password,'status': p1.status,'session':p1.session})
conn.commit()
mycursor.execute("SELECT * FROM people WHERE status='working on homework'")
print(mycursor.fetchall())
conn.commit()
conn.close()