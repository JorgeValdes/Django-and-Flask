from flask import (Flask , g , render_template, flash, url_for, redirect)
from flask_bcrypt import check_password_hash
from flask_login import LoginManager, login_user 


#Inicializo mi programa importo mis modelos y mis forms
import models
import forms

#creo mis variables de configuracion
DEBUG = True 
PORT = 8000
HOST = 'localhost'

#creo mi app
app = Flask(__name__)
app.secret_key = 'askjdaskdjskjdk'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#metodo para crear el usuario que se a creado
@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.user.id == userid)
    except models.DoesNotExist:
        return None   


#peticicon para establecer nuestra conexion a nuestra base de datos
@app.before_request
def before_request():
    """ Conecta a nuestra bd antes de cada request"""
    #if not hasattr(g, 'db'): #funcion en el caso que ya se haya conectado
    g.db = models.DATABASE
    if g.db.is_closed():
        g.db.connect()


@app.after_request
def after_request(response):    
    """ Cerramos la conexion a nuestra base de datos """
    g.db.close()
    return response


@app.route('/register', methods = ('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash('Fuiste Registrado !!', 'success')
        models.User.create_user(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form = form)



@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.loginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash('Tu nombre de usuario o contraseña no existe', 'error')
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Has iniciado sesión', 'success')
                return redirect(url_for('index'))
    return render_template('login.html', form=form)      

@app.route('/')
def index():
    """ return 'wena cabros resulto' """
    return render_template("index.html" )


if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            username='aldo',
            email='aldo1314@hotmail.com',
            password='aldo1314',
        )
    except ValueError:
        pass
    app.run(debug=DEBUG, host=HOST, port=PORT)
    