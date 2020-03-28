from collections import OrderedDict
from peewee import *
import datetime
import sys
import os
#import Entre

db = SqliteDatabase('diary.db')


class Entry(Model):
    #fechas - timestamp
    #contemido 
    """ CharField , TextField para texto las largos """
    content = TextField()
    timestamp = DateTimeField(default = datetime.datetime.now)


    class Meta:
            database = db


#metodos para nuestra clase entradas
def add_entry():
    """ Agrega un registro"""
    
    print("introduze tu registro , presiona Ctrl + d para terminar")
    data = sys.stdin.read().strip()

    if data:
        if input('Guardar entrada? [Yn]').lower() != 'n':
            Entry.create(content=data)
            print('Guardada exitosamente')


def view_entries(search_query=None):
    """ despliega nuestros entradas """
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    #print(entries)
    #recorrerlas para mostrarla de una forma bonita
 
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %D, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('+'*len(timestamp))
        #print('++++++++++++++++++')
        print(entry.content)
        print('\n\n'+'+'*len(timestamp) + '\n')
        print('n| siguiente entrada')
        print('d| borrar este registro')
        print('q| salir al menu')
        
        next_action = input('Accion a realizar: [Nq]').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)


def delete_entry(entry):
    """ borra un registro """
    response = input("Estas seguro ? [yN]").lower()
    if response == 'y':
        entry.delete_instance()

        print("Entrada borrada")
    

def buscar_entradas():
    """ buscar entradas """

    view_entries(input('Texto a buscar : '))

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', buscar_entradas),
])


def menu_loop():
    """ muestra el menu con las diferentes opciones """
        #valor vacion de None el usuario no puede haber escojido nada
    choice = None #creo la variable de eleccion 

    while choice != 'q': #mientras no aprete la q para salir
        clear()
        print("presiona 'q' para salir")
        #len = menu.items()
        for key, value in menu.items(): #ciclo for con la eleccion del diccionario
            print('{}| {}'.format(key, value.__doc__) )
        choice = input ('Eleccion: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

    print("Hasta la proxima ! uwu!")
def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    pass

    initialize()
    menu_loop()