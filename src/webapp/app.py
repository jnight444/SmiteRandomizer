from flask.app import Flask
from flask.templating import render_template

from src.random_build import RandomBuild

app = Flask(__name__)


@app.route('/')
def hello():
    build = RandomBuild()
    return render_template('index.html',
                           name=build.god.name,
                           items=[build.starter.name] + [item.name for item in build.items],
                           relics=[relic.name for relic in build.relics],
                           consumables=[consumable.name for consumable in build.consumables])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
