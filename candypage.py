import flask as fl
from flask import redirect, url_for, render_template



app = fl.Flask(__name__)


@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")

@app.route('/aboutMe')
def aboutMe():
    return render_template("aboutMe.html")


@app.route('/resume')
def resume():
    return render_template("resume.html")


@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")



@app.route('/candyCharts')
def index():
    return fl.render_template('candy-name.html')


@app.route("/<name>")
def user(name):
    # {redirect(url_for("home"))}"
    return f"Whoops! {name} is not a valid page. Click here to go back home "


if __name__ == "__main__":
    #app.run('0.0.0.0', 9001)
    app.run(debug=True)


