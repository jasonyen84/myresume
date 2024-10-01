from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import requests
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"  # 請更換為一個安全的隨機字符串
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///mydatabase.db"  # 資料庫命名為mydatabase
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 初始化數據庫
db = SQLAlchemy(app)


class User(db.Model):  # 建立User資料表-會員資料
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # 密碼加密

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


with app.app_context():  # 建立資料庫
    db.create_all()


# 註冊會員
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]

        if password != confirm_password:
            flash("密碼不匹配")
            return redirect(url_for("register"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("用戶名已存在")
            return redirect(url_for("register"))

        existing_email = User.query.filter_by(email=email).first()
        if existing_email:
            flash("電子郵件已被使用")
            return redirect(url_for("register"))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("註冊成功，請登入")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/users")
def users():
    all_users = User.query.all()
    return "<br>".join([f"{user.username} - {user.email}" for user in all_users])


# 以上為資料庫所需帶入的程式碼


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/sql")
def get_sql():
    return render_template("sql.html")


@app.route("/github")
def get_git():
    return render_template("Github.html")


@app.route("/HTML")
def get_html():
    return render_template("HTML.html")


@app.route("/css")
def get_css():
    return render_template("css.html")


@app.route("/js")
def get_js():
    return render_template("js.html")


@app.route("/pm25")
def index():
    # 从API获取数据
    url = "https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON"
    response = requests.get(url)
    data = json.loads(response.text)

    # 提取记录
    records = data["records"]

    return render_template("pm25.html", records=records)


# @app.route("/data/appinfo/str/<name>")
# def querryDataMessageByName(name):
#     print("type(name):", type(name))
#     return f"<h1>String => {name}</h1>"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            flash("登入成功")
            return redirect(url_for("home_page"))
        else:
            flash("用戶名或密碼錯誤")
            return redirect(url_for("login"))

    return render_template("login.html")


# 在 app.run() 之前添加這行
app.config["SESSION_TYPE"] = "filesystem"


if __name__ == "__main__":
    app.run(debug=True)
