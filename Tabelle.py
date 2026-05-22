import sqlite3

werte = [12, 15, 20, 22, 18, 17]

# Verbindung zur Datenbank herstellen
conn =sqlite3.connect("werte.db")

#Cursor erstellen
cursor = conn.cursor()

# Tabelle erstellen
cursor.execute("""
               CREATE TABLE IF NOT EXISTS messwerte (
               id INTEGER PRIMARY KEY AUTO_INCREMENT,
               wert INTEGER
)
""")

# Werte einfügen
for wert in werte:
    cursor.execute(
        "INSERT INTO messwerte (wert) VALUES (?)",
        (wert,)
    )

# Änderung speichern
conn.commit()

# Verbindung schließen
conn.close()

print("Werte wurden in die Datenbank gespeichert.")

# Daten auslesen
conn = sqlite3.connect("werte.db")
cursor =conn.cursor()

cursor.execute("SELECT * FROM messwerte")

daten = cursor.fetchall()

for zeile in daten:
    print(zeile)

conn.close()