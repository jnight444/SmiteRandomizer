from flask.app import Flask
from flask.templating import render_template

from src.random_build import RandomBuild

app = Flask(__name__)


@app.route('/')
def hello():
    build = RandomBuild()
    return render_template('index.html', build=build, items=[build.starter] + build.items)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
