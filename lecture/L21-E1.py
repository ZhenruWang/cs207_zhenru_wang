import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS candidates")
cursor.execute('''Create TABLE candidates (
                id INTEGER PROMARY KEY NOT NULL,
                first_name TEXT,
                last_name TEXT,
                middle_init TEXT,
                party TEXT NOT NULL)''')

db.commit()

with open("candidates.txt",'r') as candidates:
    next(candidates)
    for line in candidates.readlines():
        cid, first_name, last_name, middle_init, party = line.strip().split('|')
        val = (int(cid), first_name, last_name, middle_init, party)
        cursor.execute(''' INSERT INTO candidates
                       (id, first_name, last_name, middle_init, party)
                       VALUES(?,?,?,?,?)
                       ''', val)
        
db.commit()
db.close()