from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/index')
def index():
    param = {}
    param['zagolowok'] = "Миссия Колонизация Марса"
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')
