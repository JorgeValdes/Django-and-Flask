from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__) #inicio de la app
#route definiendo para cualquiera de mis vista

@app.route('/')
@app.route('/<name>') #define la ruta que se va a mostrar

def index(name='coke'):
    
    #name = request.args.get('name', name) #query parametros para obtener en este caso el name 
    #lastname = request.args.get('lastname', lastname) #query parametros para obtener en este caso el apellido
    context = {'name' : name}
    return render_template("index.html" , **context)
    
@app.route('/add/<float:num1>/<float:num2>') #num1 y num2 que lo recibimos como cadena de texto lo convertimos a numero




def add(num1, num2):
    suma = num1 + num2
    return render_template("add.html", numero1=num1, numero2=num2) #render_template va a el template y busca esa vista num1 pasa como parametro para el html
app.run(debug=True , port=8000 , host='localhost')

