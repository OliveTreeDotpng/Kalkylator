from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Calculation, User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

# Förklarar vad Blueprint är och varför det används. Beskriver rutten och dess koppling till HTML-sidan.
bp = Blueprint("name", __name__)

@bp.route("/")
def startpage():
    return render_template("index.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("calculator"))
        else:
            flash("Invalid username or password")
    # Sida 18 upf-5-calcing.marp.pdf
    return render_template("login.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.query.filter_by(username=username).first():
            flash("Username already exists")
            return redirect(url_for("register"))
        hashed_password = generate_password_hash(password, method="sha256")
        new_user = User(username=username, password=hashed_password)            
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successfull! Please log in.")
        return redirect(url_for("login"))
    return render_template("register.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    # Vi har inte gjort funktionen ännu
    flash("You have been logged out.")
    return redirect(url_for("login"))

@bp.route("/calculator", methods=["GET", "POST"])
@login_required
def calculator():
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            # Utvärdera uttrycket säkert
            result = eval(expression, {"__builtins__": None}, {})
            # Spara beräkningen
            new_calc = Calculation(expression=expression,
                result=str(result),
                owner=current_user)
            db.session.add(new_calc)
            db.session.commit()
            flash("Beräkning sparad!")
        except Exception as e:
            flash(f"Fel i beräkningen: {e}")
    calculations = current_user.calculations
    return render_template("calculator.html", calculations=calculations)

def save_input(user_input):
    with open("input-file.txt", "a", encoding="utf-8") as file:
        file.write(f"{user_input}\n")


