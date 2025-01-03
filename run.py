from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'test_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return self.user_id


class Texts(db.Model):
    text_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    main_text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.title


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/users")
def users():
    users = Users.query.all()
    return render_template("users.html",
                           users=users)


@app.route("/texts")
def texts():
    texts = Texts.query.all()
    return render_template("texts.html",
                           texts=texts)


@app.route("/texts/<int:text_id>/edit", methods=["GET", "POST"])
def edit_text(text_id):
    text = Texts.query.get(text_id)

    if request.method == "POST":
        # Получаем данные из формы
        text.title = request.form.get("title")
        text.main_text = request.form.get("main_text")

        # Сохраняем изменения в базе данных
        db.session.commit()
        flash("Текст успешно обновлён!", "success")
        return redirect(url_for("texts", text_id=text.text_id))

    return render_template("edit_text.html", text=text)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)