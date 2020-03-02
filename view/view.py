class View:

#contactos views
    def mostrar_contacto(self, contacto):
        print('******* Datos del contacto ******')
        print('Nombre:', contacto.nombre)
        print('Teléfono:', contacto.tel)
        print('Correo:', contacto.correo)
        print('Dirección:', contacto.dir)
        print('*********************************')

    def mostrar_contactos(self, contactos):
        print('********** CONTACTOS **********')
        for c in contactos:
            print(c.nombre, c.tel, c.correo, c.dir)
        print('*********************************')

    def agregar_contacto(self, contacto):
        print(contacto.nombre,'se ha agregado a la base de datos.')

    def borrar_contacto(self, contacto):
        print(contacto.nombre,'se ha borrado de la base de datos.')

    def actualizar_contacto(self, id_contacto):
        print('El contacto',id_contacto,'se ha modificado correctamente.')

    def contacto_ya_existe(self, contacto):
        print('EL CONTACTO',contacto.id_contacto,'YA EXISTE EN LA BASE DE DATOS.')

    def contacto_no_existe(self, id_contacto):
        print('EL CONTACTO',id_contacto.id_contacto,'NO EXISTE EN LA BASE DE DATOS.')

#cita views
    def mostrar_cita(self, cita):
        print('********* Datos de la cita **********')
        print('Lugar:', cita.lugar)
        print('Fecha:', cita.fecha)
        print('Hora:', cita.hora)
        print('Dirección:', cita.asunto)
        print('*************************************')

    def mostrar_citas(self, citas):
        print('*************** CITAS ***************')
        for c in citas:
            print(c.lugar, c.fecha, c.hora, c.asunto)
        print('*************************************')

    def agregar_cita(self, cita):
        print('La cita', cita.id_cita, cita.lugar, 'se ha agregado a la base de datos')

    def borrar_cita(self, cita):
        print('La cita', cita.id_cita, cita.lugar, 'se ha borrado de la base de datos')

    def actualizar_cita(self, id_cita):
        print('la cita', id_cita,'se ha modificado correctamente.')

    def cita_ya_existe(self, cita):
        print('La cita', cita.id_cita,'YA EXISTE EN LA BASE DE DATOS.')

    def cita_no_existe(self, id_cita):
        print('La cita', id_cita.id_cita,'NO EXISTE EN LA BASE DE DATOS.')

#General views
    def start(self):
        print('Esto es un ejemplo de vista sencillo.')

    def end(self):
        print('¡Hasta la vista!')

    def opcion_no_valida(self):
        print('Opción no valida')

    def menu(self):
        print('************ MENU ************')
        print('Contactos')
        print('1) Agregar contacto')
        print('2) Mostrar contacto')
        print('3) Mostrar todos los contactos')
        print('4) Actualizar contacto')
        print('5) Borrar contacto')
        print('6) Mostar contactos con la letra')
        print('Citas')
        print('7) Agregar cita')
        print('8) Mostrar cita')
        print('9) Mostrar todas las citas')
        print('10) Actualizar cita')
        print('11) Borrar cita')
        print('12) Mostrar citas por fecha')
        print('13) Salir')