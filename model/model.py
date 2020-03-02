from .contacto import Contacto
from .cita import Cita

class Model:

    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id_contacto(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0

    def esta_id_cita(self, id_cita):
        for cita in self.citas:
            if cita.id_cita == id_cita:
                return True, cita
        return False, 0

    #Contacto methods
    def agregar_contacto(self, id_contacto, nombre, tel, correo, dir):
        if not self.esta_id_contacto(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, dir)
            self.contactos.append(c)
            return True, c
        return False, c
    
    def leer_contacto(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        return e, c

    def leer_todos_contactos(self):
        return self.contactos

    def actualizar_contacto(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir = ''):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            if n_nombre != '':
                c.nombre = n_nombre
            if n_tel != '':
                c.tel = n_tel
            if n_correo != n_correo:
                c.correo = n_correo
            if n_dir != '':
                c.dir = n_dir
            return True
        return False

    """def actualizar_contacto_elementos_2(self, id_contacto, n_nombre = '', n_tel = '', n_correo = '', n_dir  =''):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            c.nombre = n_nombre
            c.tel = n_tel
            c.correo = n_correo
            c.dir = n_dir
            return True"""

    """def actualizar_contacto_elementos(self, id_contacto):
        e, c = self.esta_id_contacto(id_contacto)
        if e:
            opc = input('¿Qué desea actualizar? ')
            opc = opc.lower()
            if opc == 'nombre':
                n_nombre = input('Ingrese el nuevo nombre: ')
                c.nombre = n_nombre
            if opc == 'tel':
                n_tel = input('Ingrese el nuevo tel: ')
                c.tel = n_tel
            if opc == 'correo':
                n_correo = input('Ingrese el nuevo correo: ')
                c.correo = n_correo
            if opc == 'dir':
                n_dir = input('Ingrese la nueva dir: ')
                c.dir = n_dir
            return True"""

    def borrar_contacto(self, id_contacto):
        e, contacto = self.esta_id_contacto(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]
            for c in lista_temp:
                self.citas.remove(c)
            return True, contacto
        return False, 0

    """def buscar_contacto(self):
        b_ini = input('Ingrese la letra incial del nombre a buscar: ')
        b_ini = b_ini.upper()
        c_lista = []
        for c in self.contactos:
            if c.nombre[0] == b_ini:
                c_lista.append(c.nombre)
        print(c_lista)"""

    #Es la de buscar contactos por letra
    def leer_contactos_letra(self, letra):
        lista = [c for c in self.contactos if c.nombre.lower().startswith(letra)]
        #lista = []
        #for c in self.contactos:
        #    if c.nombre[0] == letra:
        #    #if c.nombre.lower().starswith(letra):
        #        lista.append(c)
        return lista

    #Cita methods
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        if not self.esta_id_cita(id_cita)[0]:
            cita = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
            self.citas.append(cita)
            return True, cita
        return False, cita

    def leer_cita(self, id_cita):
        ec, cita = self.esta_id_cita(id_cita)
        return ec, cita

    def leer_todas_citas(self):
        return self.citas

    def actualizar_cita(self, id_cita, n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        ec, cita = self.esta_id_cita(id_cita)
        if ec:
            if n_lugar != '':
                cita.lugar = n_lugar
            if n_fecha != '':
                cita.fecha = n_fecha
            if n_hora != '':
                cita.hora = n_hora
            if n_asunto != '':
                cita.asunto = n_asunto
            return True
        return False

    """def actualizar_cita_elementos(self, id_cita, id_contacto, n_lugar = '', n_fecha = '', n_hora = '', n_asunto = ''):
        ec, cita = self.esta_id_cita(id_cita)
        if ec:
            e, c = self.esta_id_contacto(id_contacto)
            if e:
                cita.lugar = n_lugar
                cita.fecha = n_fecha
                cita.hora = n_hora
                cita.asunto = n_asunto
                return True"""

    """def actualizar_citas_elementos(self, id_cita):
        ec, cita = self.esta_id_cita(id_cita)
        if ec:
            opc = input('¿Qué desea actualizar? ')
            opc = opc.lower()
            if opc == 'lugar':
                n_lugar = input('Ingrese el nuevo lugar: ')
                cita.lugar = n_lugar
            if opc == 'fecha':
                n_fecha = input('Ingrese el nuevo fecha: ')
                cita.fecha = n_fecha
            if opc == 'hora':
                n_hora = input('Ingrese el nuevo hora: ')
                cita.hora = n_hora
            if opc == 'asunto':
                n_asunto = input('Ingrese la nueva asunto: ')
                cita.asunto = n_asunto
            return True"""

    def borrar_cita(self, id_cita):
        ec, cita = self.esta_id_cita(id_cita)
        if ec:
            self.citas.remove(cita)
            return True, cita
        return False, cita

    #def buscar_cita_fecha(self):
    #    b_fecha = input('Ingrese la fecha a buscar(dd-mm-aaaa): ')
    #    for c in self.citas:
    #        if b_fecha == c.fecha:
    #            print(c.lugar)

    #Busca la cita por fecha
    def leer_citas_fecha(self, fecha):
        lista = [ c for c in self.citas if c.fecha == fecha]
        #lista = []
        #for c in self.citas:
        #    if c.fecha == fecha:
        #        lista.append(c)
        return lista

