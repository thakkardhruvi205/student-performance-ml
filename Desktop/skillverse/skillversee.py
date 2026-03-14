from flask import Flask, render_template, request, redirect, session
import sqlite3
import cv2

app = Flask(__name__)
app.secret_key = "skillverse_secret"

DB_NAME = "dataaaabasee.db"

# ==========================
# DATABASE INIT
# ==========================
def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        score INTEGER DEFAULT 0
    )
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS skills(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        skill_name TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ==========================
# ROUTES
# ==========================

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]

        if "indusuni.ac.in" not in email:
            return "Use valid College Email"

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE email=?",(email,)).fetchone()

        if not user:
            conn.execute("INSERT INTO users (email) VALUES (?)",(email,))
            conn.commit()

        conn.close()
        session["user"] = email
        return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    conn = get_db()
    skills = conn.execute("SELECT * FROM skills WHERE user_email=?",
                          (session["user"],)).fetchall()
    user = conn.execute("SELECT * FROM users WHERE email=?",
                        (session["user"],)).fetchone()
    conn.close()

    return render_template("dashboard.html",
                           email=session["user"],
                           skills=skills,
                           score=user["score"])

@app.route("/add_skill", methods=["POST"])
def add_skill():
    skill = request.form["skill"]

    conn = get_db()
    conn.execute("INSERT INTO skills (user_email, skill_name) VALUES (?,?)",
                 (session["user"], skill))
    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")
    return render_template("profile.html", email=session["user"])

@app.route("/test/<skill>")
def test(skill):
    return render_template("test.html", skill=skill)

# ==========================
# AI ANTI CHEAT (OpenCV)
# ==========================
def monitor_cheating():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    cheat_score = 0
    frames = 0

    while frames < 80:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            cheat_score += 2
        elif len(faces) > 1:
            cheat_score += 3

        cv2.imshow("AI Monitoring - Press ESC to stop", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        frames += 1

    cap.release()
    cv2.destroyAllWindows()
    return cheat_score

@app.route("/submit_test", methods=["POST"])
def submit_test():

    q1 = int(request.form.get("q1", 0))
    q2 = int(request.form.get("q2", 0))
    q3 = int(request.form.get("q3", 0))

    test_score = (q1 + q2 + q3) * 30

    cheat_score = monitor_cheating()

    final_score = test_score - cheat_score
    if final_score < 0:
        final_score = 0

    conn = get_db()
    conn.execute("UPDATE users SET score=? WHERE email=?",
                 (final_score, session["user"]))
    conn.commit()
    conn.close()

    return redirect("/leaderboard")

@app.route("/leaderboard")
def leaderboard():
    conn = get_db()
    users = conn.execute("SELECT * FROM users ORDER BY score DESC").fetchall()
    conn.close()
    return render_template("leaderboard.html", users=users)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)