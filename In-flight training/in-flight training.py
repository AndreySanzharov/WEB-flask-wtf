from flask import Flask
from flask import url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/training/<prof>')
def prof_training(prof):
    prof = prof.lower()
    profession = ""
    image = "ship.jpg"
    if prof == "врач":
        profession = "Научные симуляторы"
        image = "interstellar.jpg"
    elif "инжинер" in prof or "строитель" in prof:
        profession = "Инжинерные тренажёры"
        image = "falcon.jpg"
    return render_template('training.html', profession=profession, image=url_for('static', filename='images/' + image))


if __name__ == "__main__":
    app.run(port=8000, host='127.0.0.1')
