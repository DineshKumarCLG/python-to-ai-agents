import sqlite3

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT
    );
""")

cursor.execute("INSERT INTO expenses (category, amount, description) VALUES (?, ?, ?)",
("Transport", 45.0, "Bus"))

conn.commit()

cursor.execute("SELECT * FROM expenses WHERE category = ?", ("Transport",))
rows = cursor.fetchall()
print(rows)

conn.close()