import sqlite3

conn = sqlite3.connect("veritabani.db")
cursor = conn.cursor()

try:
    cursor.execute("ALTER TABLE kullanicilar ADD COLUMN para INTEGER DEFAULT 1000")
    cursor.execute("ALTER TABLE kullanicilar ADD COLUMN altin INTEGER DEFAULT 0")
    cursor.execute("ALTER TABLE kullanicilar ADD COLUMN gen_puani INTEGER DEFAULT 0")
    conn.commit()
except Exception as e:
    print("Alanlar zaten ekli olabilir:", e)

conn.close()