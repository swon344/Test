import sqlite3

def veritabani_olustur():
    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kullanici_adi TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    sifre TEXT NOT NULL,
    para INTEGER DEFAULT 100,
    altin INTEGER DEFAULT 0,
    gen_puani INTEGER DEFAULT 0,
    tarla1 INTEGER DEFAULT 1,
    tarla2 INTEGER DEFAULT 0,
    tarla3 INTEGER DEFAULT 0,
    tarla4 INTEGER DEFAULT 0,
    tarla5 INTEGER DEFAULT 0,
    tarla6 INTEGER DEFAULT 0,
    tarla7 INTEGER DEFAULT 0,
    tarla8 INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
