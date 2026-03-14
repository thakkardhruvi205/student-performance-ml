from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3
from app.face_auth import capture_face, verify_face

routes = Blueprint("routes", __name__)

DATABASE = "database.db"


def get_db():

    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@routes.route("/")
def home():
    return render_template("home.html")


# ---------------- REGISTER ----------------

@routes.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")
        department = request.form.get("department")

        if not email or not password or not department:
            return "All fields are required!"

        if "indusuni.ac.in" not in email:
            return "Only Indus University email allowed"

        conn = get_db()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (email,password,department,team,score) VALUES (?,?,?,?,?)",
            (email, password, department, "Not Assigned", 0),
        )

        conn.commit()
        conn.close()

        capture_face(email)

        return redirect(url_for("routes.login"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@routes.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db()
        cur = conn.cursor()

        user = cur.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password),
        ).fetchone()

        conn.close()

        if not user:
            return "Invalid login"

        if not verify_face(email):
            return "Face verification failed"

        return redirect(url_for("routes.dashboard"))

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")