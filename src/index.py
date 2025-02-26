import flask # type: ignore

app = flask.Flask(__name__)

@app.route('/')
def index():
    return '<h3>Hello, World!</h3>'

if __name__ == '__main__':
    app.run()