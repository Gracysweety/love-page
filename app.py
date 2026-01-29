from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # can be anything

PASSWORD = "Calebsweetyloves"  # 🔑 CHANGE THIS PASSWORD

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        entered_password = request.form.get("password")

        if entered_password == PASSWORD:
            session["logged_in"] = True
            return redirect(url_for("love"))
        else:
            return render_template("login.html", error="Wrong password 💔")

    return render_template("login.html")

@app.route("/love")
def love():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

