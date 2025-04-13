import sqlite3

def veritabani_olustur():
    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT UNIQUE NOT NULL,
            sifre TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
