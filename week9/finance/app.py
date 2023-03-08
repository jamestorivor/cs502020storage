import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
import re
from helpers import apology, login_required, lookup, usd


def check_password(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"\W", password) is None
    check_password = not (length_error or digit_error or uppercase_error or lowercase_error or symbol_error)
    return check_password


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    prices = {}
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    total = db.execute(
        "SELECT symbol,SUM(quantity_bought),stock_name FROM users JOIN stocks ON users.id = stocks.id WHERE users.id = ? GROUP BY symbol", session["user_id"])
    length = len(total)
    sum_total = cash[0]["cash"]
    for row in range(length):
        data = lookup(total[row]["symbol"])
        prices[total[row]["symbol"]] = data["price"]
        sum_total += (data["price"] * total[row]["SUM(quantity_bought)"])

    return render_template("index.html", total=total, length=length, prices=prices, cash=cash, sum_total=sum_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        data = lookup(request.form.get("symbol"))
        if not data:
            return apology("Invalid symbol", 400)
        elif not request.form.get("shares").isdigit():
            return apology("Invalid number of shares", 400)
        else:
            total_price = int(request.form.get("shares")) * data["price"]
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            remainder = float(cash[0]["cash"]) - total_price
            if remainder < 0:
                return apology("Error, not enough cash", 400)
            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?", remainder, session["user_id"])
                db.execute("INSERT INTO stocks (id, stock_name ,quantity_bought ,price ,symbol,total_price, date) VALUES (?,?,?,?,?,?,?)", session["user_id"], data["name"], int(
                    request.form.get("shares")), data["price"], data["symbol"], total_price, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    table = db.execute("SELECT symbol, quantity_bought, price, date FROM stocks WHERE id = ?", session["user_id"])
    tablelen = len(table)
    return render_template("history.html", tablelen=tablelen, table=table)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not lookup(request.form.get("symbol")):
            return apology("Invalid Symbol", 400)
        else:
            data = lookup(request.form.get("symbol"))
            return render_template("quoted.html", name=data["name"], price=data["price"], symbol=data["symbol"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").lower())

        if not request.form.get("username").lower():
            return apology("Please input a username", 400)
        elif len(rows) != 0:
            return apology("Username taken", 400)
        elif (request.form.get("password") != request.form.get("confirmation")):
            return apology("passwords do not match", 400)
        elif not request.form.get("password") or not request.form.get("confirmation"):
            return apology("Please input a password and confirm it", 400)

        else:
            if check_password(request.form.get("password")) == False:
                flash("Your password must be at least 8 characters long with 1 Uppercase letter, 1 lowercase letter, 1 digit and 1 special character")
                return render_template("register.html")
            else:
                hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
                db.execute("INSERT INTO users (username, hash) VALUES (? ,?) ", request.form.get("username").lower(), hash)
                return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    symbols = db.execute("SELECT symbol,SUM(quantity_bought) FROM stocks WHERE id = ? GROUP BY symbol", session["user_id"])
    sym_len = len(symbols)
    if request.method == "POST":
        nsym = {}
        for row in range(sym_len):
            nsym[symbols[row]["symbol"]] = symbols[row]["SUM(quantity_bought)"]
        if int(request.form.get("shares")) > nsym[request.form.get("symbol")]:
            return apology("Invalid number of shares",  400)
        else:
            data = lookup(request.form.get("symbol"))
            total_price = int(request.form.get("shares")) * data["price"]
            cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            remainder = float(cash[0]["cash"]) + (int(request.form.get("shares")) * data["price"])
            db.execute("UPDATE users SET cash = ? WHERE id =?", remainder, session["user_id"])
            db.execute("INSERT INTO stocks (id, stock_name ,quantity_bought ,price ,symbol,total_price, date) VALUES (?,?,?,?,?,?,?)",
                       session["user_id"], data["name"], -int(request.form.get("shares")), data["price"], data["symbol"], total_price, datetime.datetime.now().strftime('%Y-%m-%d'))
            return redirect("/")
    else:
        return render_template("sell.html", symbols=symbols, sym_len=sym_len)
