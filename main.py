from flask import Flask, render_template
from register import RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello hello hello hello"


@app.route("/")
def index():
    return render_template('base.html', title="Главная страница 2.0")

@app.route("/reg", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template("reg.html", form=form)


@app.route('/stud')
def students():
    list_students = ['Кирилл Тетюев', 'Евгений Сожевский', 'Нистрян Даниел',
                     'Андрей Коротий', 'Нистрян Даниел', 'Мардан Адилханов',
                     'Аслан Аксиров']
    return render_template('students.html', title='Список студентов',
                           data=list_students)


@app.route("/info")
def info():
    return "<h3>Сайт создан компанией GeekBrains</h3>"



@app.route("/calc/<int:x>/<int:y>")
def calc(x, y):
    return f'{x} + {y} = {x + y}'


@app.route("/hi/<name>")
def hello(name):
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run()
