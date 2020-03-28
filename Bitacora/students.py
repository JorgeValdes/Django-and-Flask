from peewee import *
import peewee as pw

db = SqliteDatabase('students.db')

""" 
    #myDB = pw.MySQLDatabase(host="localhost",port=3306,user="user",passwd="password",db="students")
    #mysql_db = MySQLDatabase('students.db')

    prueba para base de datos en mysql

    mysql_db = MySQLDatabase('my_database')

class BaseModel(Model):
 
    class Meta:
        database = mysql_db

class User(BaseModel):
    username = CharField()
    # etc, etc

    # Connect to a MySQL database on network.
mysql_db = MySQLDatabase('my_app', user='app', password='db_password',
                         host='10.1.0.8', port=3306)
 """
 

#definicion de nuestros modelos

class Student(Model):
    
    username = CharField(max_length=225, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db


students = [
    {'username' : 'cooke',
      'points' :  3,
    },
    {
        'username' : 'aldo',
        'points' : 10,
    },
    {
        'username' : 'jorge',
        'points' : 40,
    },
    {
        'username' : 'chabe',
        'points' : 50,
    }

]

def add_students():

    for student in students:
        try:

            Student.create(username = student['username'],
                        points = student['points'])

        #en el caso que ya este registrado el error se modificara solamente la puntuacion de este 
        except IntegrityError:
            #print("hubo algun error")
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            #cualquier registro para la base de datos se utiliza save
            student_record.save()

#defino un metodo para tener el alumno con el mayor registro de puntuacion el .get me trae solamente un registro
def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    return student

if __name__ == '__main__':

    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("obtener el mayor alumno con puntuacion : {}" .format(top_student().username))
    print("ejecutado con exito , no hubo ningun error")

