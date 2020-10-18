import flask as fl

app = fl.Flask(__name__)


@app.route('/')
def index():
    return fl.render_template('candy-name.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 9001)
