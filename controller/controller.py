from model.model import Model
from view.view import View

class Controller:

    #Constructor
    def __init__(self):
        self.model = Model()
        self.view = View()

    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        e, c = self.model.agregar_contacto(id_contacto, nombre, tel, correo, dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)

    def leer_contacto(self, id_contacto):
        e, c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)

    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)

    def leer_contactos_letra(self, letra):
        c = self.model.leer_contactos_letra(letra)
        self.view.mostrar_contactos(c)

    #cita controllers
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            self.view.cita_ya_existe(c)
    
    def leer_cita(self, id_cita):
        e, c = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)
    
    def leer_todas_citas(self):
        c = self.model.leer_todas_citas()
        self.view.mostrar_citas(c)

    def actualizar_cita(self, id_cita, n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        e = self.model.actualizar_cita(id_cita, n_lugar, n_fecha, n_lugar, n_asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_ya_existe(id_cita)

    def borrar_cita(self, id_cita):
        e, c = self.model.borrar_cita(id_cita)
        if e:
            self.view.borrar_cita(c)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas_fecha(self, fecha):
        c = self.model.leer_citas_fecha(fecha)
        self.view.mostrar_citas(c)

    #General methods
    def insertar_contactos(self):
        self.agregar_contacto(1, 'Jorge Manriquez', '464-124-3720', 'j@gmail.com', 'Tlamacas #321')
        self.agregar_contacto(2, 'Lana Torres', '464-567-2342', 'at@ugto.mx', 'Sendero #123')
        self.agregar_contacto(3, 'Lizeth Tapia', '464-123-4567', 'lt@ugto.mx', 'Camino #456')

    def insertar_citas(self):
        self.agregar_cita(1, 1, 'Aula 310', '20-02-2020', '14:00', 'Clase de Sistemas de Información')
        self.agregar_cita(2, 2, 'Aula 311', '21-02-2020', '15:00', 'Clase de Inteligencia Artificial')
        self.agregar_cita(3, 1, 'Aula 312', '21-02-2020', '15:30', 'Clase de Calculo Vectorial')

    def start(self):
        #Diplay a welcome message
        self.view.start()
        #Insert data i model
        """self.insertar_contactos()
        self.insertar_citas()"""
        self.menu()
        #Show all contacts in DB
        """self.leer_todos_contactos()
        self.leer_contactos_letra('l')
        self.leer_todas_citas()"""
        self.view.end()

    def menu(self):
        #Display menu
        self.view.menu()
        while True:
            o = input('Selecciona una opción (1-13): ')
            if o == '1':
                id_contacto = input('ID: ')
                nombre = input('Nombre: ')
                tel = input('Teléfono: ')
                correo = input('Correo: ')
                dir = input('Dirección: ')
                self.actualizar_contacto(id_contacto, nombre, tel, correo, dir)
                #self.insertar_contactos()
            elif o == '2':
                id_contacto = int(input('Ingrese el id del contacto: '))
                self.leer_contacto(id_contacto)
            elif o == '3':
                self.leer_todos_contactos()
            elif o == '4':
                self.actualizar_contacto(1, n_nombre='Luis Manriquez')
            elif o == '5':
                id_contacto = int(input('Ingrese el id del contacto: '))
                self.borrar_contacto(id_contacto)
            elif o == '6':
                letra = input('Ingrese la letra: ')
                self.leer_contactos_letra(letra.lower())
            elif o == '7':
                self.insertar_citas()
            elif o == '8':
                id_cita = int(input('Ingrese el id de la cita: '))
                self.leer_cita(id_cita)
            elif o == '9':
                self.leer_todas_citas()
            elif o == '10':
                self.actualizar_cita(1, n_asunto='Clase de Aplicaciones')
            elif o == '11':
                id_cita = int(input('Ingrese el id de la cita: '))
                self.borrar_cita(id_cita)
            elif o == '12':
                fecha = input('Ingrese la fecha (dd-mm-aaaa): ')
                self.leer_citas_fecha(fecha)
            elif o == '13':
                break
            else:
                self.view.opcion_no_valida()