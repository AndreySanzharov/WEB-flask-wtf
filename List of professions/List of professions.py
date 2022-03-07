from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/list_prof/<type>')
def profession_list(type):
    if type not in ["ul", "ol"]:
        return render_template("training.html")

    profession_list = [
        "инженер-исследователь", "пилот", "строитель",
        "экзобиолог", "врач", "инженер по терраформированию",
        "климатолог", "специалист по радиацинной защите", "астрогеолог",

    ]
    return render_template('base.html', type_=type,
                           profession_list=profession_list)


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')
