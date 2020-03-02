from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller

"""
contactos = []
c1 = Contacto(1, 'Jorge Manriquez', '464-124-3720', 'j@gmail.com', 'Tlamacas #321')
c2 = Contacto(2, 'Ana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero #123')

t1 = Cita(1, 1, "Aula 310", '20-02-2020', '14:00', 'Clase de Sistemas de Información')

contactos.append(c1)
contactos.append(c2)

t = input('Dame un nombre: ')

for c in contactos:
    if t.lower() == c.nombre.lower():
        print('Si esta')
        break
else:
    print('No esta')
"""

"""m = Model()

#Agrega un nuevo contacto
m.agregar_contacto(1, 'Jorge Manriquez', '464-124-3720', 'j@gmail.com', 'Tlamacas #321')
m.agregar_contacto(2, 'Lana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero #123')
m.agregar_contacto(3, 'Lizeth Tapia', '464-123-4567', 'lt@ugto.mx', 'Camino #456')"""

"""
#Lee un contacto
s = m.leer_contacto(2)
print(s.nombre)

#Actualiza un elemento del contacto
m.actualizar_contacto_elementos(2)
s = m.leer_contacto(2)
print(s.nombre)
s = m.leer_contacto(2)
print(s.nombre)

#Actualiza todos los elementos del contacto
m.actualizar_contacto(2, 'Sara Juarez', '123-456-7894', 'sj@gmail.com', 'Sin direccion')
s = m.leer_contacto(2)
print(s.nombre)

#Borra un contacto
s = m.borrar_contacto(1)
print(s)
s = m.borrar_contacto(1)
print(s)
"""
#Agrega una cita nueva
"""m.agregar_cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Información')
m.agregar_cita(2, 2, 'Aula 311', '21-02-2020', '15:00', 'Clase de Inteligencia Artificial')
m.agregar_cita(3, 1, 'Aula 312', '21-02-2020', '15:30', 'Clase de Calculo Vectorial')"""
"""
#Lee una cita
t1 = m.leer_cita(1)
t2 = m.leer_cita(2)
print(t1.lugar)
print(t2.lugar)

#Actualiza todos los elementos de la cita
m.actualizar_cita(2,'Aula 210', '30-02-2020', '20:00', 'Clase de Base de Datos')
t2 = m.leer_cita(2)
print(t2.lugar)

#Borra una cita
t2 = m.borrar_cita(2)
print(t2)
t2 = m.borrar_cita(2)
print(t2)
"""
#Busca todos los contactos por la primera letra
#m.buscar_contacto()

#Busca las citas de la misma fecha
#m.buscar_cita_fecha()

#s = m.leer_citas_fecha('21-02-2020')
#for i in s:
#    print(i.lugar, i.asunto)
#
#s = m.borrar_contacto(1)
#for i in s:
#    print()
##################################
"""l = m.leer_todas_citas()
for c in l:
    print(c.fecha, c.hora, c.asunto)

v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)

s = m.leer_todos_contactos()
v.mostrar_contactos(s)"""

"""v = View()
s = m.leer_todas_citas()
v.mostrar_citas(s)

c = m.leer_cita(1)
v.mostrar_cita(c)

f = m.borrar_cita(1)
if f:
    v.borrar_cita(c)
else:
    v.cita_no_existe(c)

s = m.leer_todas_citas()
v.mostrar_citas(s)"""

cont = Controller()
cont.start()