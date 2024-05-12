#Импорт
from flask import Flask, render_template,request, redirect
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы

class Card(db.Model):
    #Создание полей
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Заголовок
    title = db.Column(db.String(100), nullable=False)
    #Описание
    subtitle = db.Column(db.String(300), nullable=False)
    #Текст
    text = db.Column(db.Text, nullable=False)

    #Вывод объекта и id
    def __repr__(self):
        return f'<Card {self.id}>'
    

#Задание №1. Создать таблицу User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(30), nullable=False)







#Запуск страницы с контентом
@app.route('/', methods=['GET','POST'])
def login():
        error = ''
        if request.method == 'POST':
            form_login = request.form['email']
            form_password = request.form['password']
            
            #Задание №4. Реализовать проверку пользователей
            users_db = User.query.all()
            for user in users_db:
                if form_login == user.login and form_password == user.password:
                    return redirect('/index')
            else:
                error = 'Неправильно указан пользователь или пароль'
                return render_template('login.html', error=error)

            
        else:
            return render_template('login.html')



@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        login= request.form['email']
        password = request.form['password']
        
        #Задание №3. Реализовать запись пользователей
        user = User(login=login, password=password)
        db.session.add(user)
        db.session.commit()
        
        return redirect('/')
    
    else:    
        return render_template('registration.html')


#Запуск страницы с контентом
@app.route('/index')
def index():
    #Отображение объектов из БД
    cards = Card.query.order_by(Card.id).all()
    return render_template('index.html', cards=cards)

#Запуск страницы c картой
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Запуск страницы c созданием карты
@app.route('/create')
def create():
    return render_template('create_card.html')

#Форма карты
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Создание объкта для передачи в дб

        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('create_card.html')





if __name__ == "__main__":
    app.run(debug=True)
        


        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
