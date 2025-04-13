from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def ana_sayfa():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Burada kullanıcı kontrolü yapılabilir
        return f"Hoş geldin, {username}!"  # Geçici olarak yazıyoruz
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Burada kullanıcıyı veritabanına kaydedebilirsin
        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
