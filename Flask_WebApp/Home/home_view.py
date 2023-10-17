from flask import Flask, request, url_for, render_template, redirect, Blueprint

home_page = Blueprint("home_page", __name__, template_folder="home_templates")

app = Flask(__name__)

# 127.0.0.1:5000/Home
@app.route("/")
@app.route("/Home")
def index():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)

