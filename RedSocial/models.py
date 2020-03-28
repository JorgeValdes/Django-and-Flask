from peewee import * #para poder usar la base de datos
import datetime #PARA PODER TRABAJAR CON LAS FECHAS
from collections import OrderedDict # PARA PODER USAR EL MENU
from flask_bcrypt import generate_password_hash  #ES UNA LIBRERIA DE FLASK PARA PROTEGER CONTRASEÑAS ETC

#base de datos donde sera almacenado nuestra informacion
DATABASE = SqliteDatabase('social.db')


#flask_bcrypt import generate_password_hash una libreria que sirve para la encryptacion
class User(Model):

    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=4)
    joined_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at')
    
    @classmethod #metodo de la clase instancia
    def  create_user(cls, username, email, password):
        try:
            cls.create(
                username = username,
                email = email,
                password = generate_password_hash(password),
            )
        except IntegrityError:
            raise ValueError('User already exists')



def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
