from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("home.html")


@app.route("/hello")
def hello():
    return "<h1>Hello</h1>"


@app.route("/<name>")
def by_name(name):
    return f"<h1>{name}, Welcome. This is my Home Page!</h1>"


@app.route("/data/appinfo/str/<name>")
def querryDataMessageByName(name):
    print("type(name):", type(name))
    return f"<h1>String => {name}</h1>"


if __name__ == "__main__":
    app.run()
