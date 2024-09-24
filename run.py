from flask import Flask, render_template
import requests
import json

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


if __name__ == "__main__":
    app.run(debug=True)
