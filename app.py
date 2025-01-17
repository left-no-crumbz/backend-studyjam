import os

import sqlalchemy as sa
from dotenv import load_dotenv
from extensions import db
from flask import Flask, redirect, render_template, url_for
from forms import QuestionForm
from models import QuestionModel

app = Flask(__name__)
load_dotenv()
SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess this"
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    queries = [
        {
            "asker": "Anonymous1",
            "question": "What's your name?",
        },
        {
            "asker": "Anonymous2",
            "question": "What's your fave dessert?",
        },
    ]
    form = QuestionForm()

    if form.validate_on_submit():
        # add database actions here
        question = QuestionModel(
            username=form.username.data,  # type: ignore
            question=form.question.data,  # type: ignore
        )

        db.session.add(question)
        db.session.commit()
        return redirect(url_for("index"))

    queries = db.session.scalars(
        sa.select(QuestionModel).order_by(QuestionModel.timestamp)
    )

    return render_template("index.html", queries=queries, form=form)


if __name__ == "__main__":
    # Creates the db
    with app.app_context():
        db.create_all()

    app.run(debug=True)
