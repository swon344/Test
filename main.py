from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import veritabani_olustur
import sqlite3

veritabani_olustur()
app = Flask(__name__)
app.secret_key = "gizli_anahtar"

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        sifre = request.form[("sifre")]

        conn = sqlite3.connect("veritabani.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kullanicilar WHERE email = ? AND sifre = ?", (email, sifre))
        kullanici = cursor.fetchone()
        conn.close()

        if kullanici:
            session["kullanici_id"] = kullanici[0]
            session["kullanici_adi"] = kullanici[1]
            flash(f"Giriş başarılı! Hoş geldin, {kullanici[1]}", "success")
            return redirect(url_for("oyun_ekrani"))
        else:
            flash("Hatalı e-posta ya da şifre.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        kullanici_adi = request.form["kullanici_adi"]
        email = request.form["email"]
        sifre = request.form["sifre"]

        # Veritabanına kayıt ekle
        try:
            conn = sqlite3.connect("veritabani.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO kullanicilar (kullanici_adi, email, sifre) VALUES (?, ?, ?)",
                           (kullanici_adi, email, sifre))
            conn.commit()
            conn.close()

            flash("Kayıt başarıyla tamamlandı! Giriş yapabilirsiniz.", "success")
            return redirect(url_for("login"))

        except sqlite3.IntegrityError:
            flash("Bu e-posta adresi zaten kayıtlı!", "danger")
            return redirect(url_for("register"))

    return render_template("register.html")

@app.route("/game")
def oyun_ekrani():
    if "kullanici_id" not in session:
        flash("Lütfen önce giriş yapınız.", "warning")
        return redirect(url_for("login"))

    kullanici_id = session["kullanici_id"]
    conn = sqlite3.connect("veritabani.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT kullanici_adi, tarla1, tarla2, tarla3, tarla4, tarla5, tarla6, tarla7, tarla8, para, altin, gen_puani 
    FROM kullanicilar 
    WHERE id = ?
    """, (kullanici_id,))
    veri = cursor.fetchone()

    kullanici_bilgileri = {
        "kullanici_adi": veri[0],
        "tarla1": veri[1],
        "tarla2": veri[2],
        "tarla3": veri[3],
        "tarla4": veri[4],
        "tarla5": veri[5],
        "tarla6": veri[6],
        "tarla7": veri[7],
        "tarla8": veri[8],
        "para": veri[9],
        "altin": veri[10],
        "gen_puani": veri[11]
    }

    tarlalar = [veri[1], veri[2], veri[3], veri[4], veri[5], veri[6], veri[7], veri[8]
    ]

    conn.close()

    tarla_durumlari = []
    for tarla in tarlalar:
        if tarla != 0:
            tarla_durumlari.append(tarla)

    return render_template("game.html", kullanici_adi=session["kullanici_adi"], tarlalar=tarla_durumlari, kullanici_bilgileri=kullanici_bilgileri)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
