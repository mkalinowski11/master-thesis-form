from flask import Flask, request, render_template, redirect, url_for
import os
from models import db, Response

VOICE_DATA = os.path.join('static', 'voice_data')
app = Flask(__name__)
app.secret_key = 'abracadabra'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

def parse_answers(answers):
    if not any(map(lambda a : len(a) == 0, answers)):
        return True
    else:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = []
        for spk_id in os.listdir(VOICE_DATA):
            data.append(request.form.get(spk_id))
        if parse_answers(data):
            data = list(map(lambda a: int(a), data))
            response = Response(*data)
            db.session.add(response)
            db.session.commit()
            print(f'Succesfully added data: {data}')
            return redirect(url_for("end_form"))
    return render_template(
            "voice_form.html",
            title="Weryfikacja jakości konwersji głosu",
            speaker_data = os.listdir(VOICE_DATA),
            samples = os.listdir(os.path.join(
                VOICE_DATA, os.listdir(VOICE_DATA)[0]
            ))
        )

@app.route("/end-form")
def end_form():
    return render_template("info.html", title = "Dziękuję za wypełnienie formularza")

if __name__ == "__main__":
    app.run(debug=True)