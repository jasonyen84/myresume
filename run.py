from flask import Flask, render_template

app = Flask(__name__)


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


# @app.route("/data/appinfo/str/<name>")
# def querryDataMessageByName(name):
#     print("type(name):", type(name))
#     return f"<h1>String => {name}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
