from src.utils.validaciones import (
    enmascarar_dni, validar_dni, validar_telefono, validar_texto,
)


class Paciente:
    def __init__(self, id_paciente, nombre, apellido, dni, telefono):
        self.__id_paciente = id_paciente
        self.__nombre = validar_texto(nombre, "nombre")
        self.__apellido = validar_texto(apellido, "apellido")
        self.__dni = validar_dni(dni)
        self.__telefono = validar_telefono(telefono)
        self.__atenciones = []  # Composición: las atenciones pertenecen al paciente

    @property
    def id_paciente(self):
        return self.__id_paciente

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def dni(self):
        return self.__dni

    @property
    def dni_enmascarado(self):
        return enmascarar_dni(self.__dni)

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def registrar_paciente(self):
        return f"Paciente registrado: {self.__nombre} {self.__apellido} (DNI {self.dni_enmascarado})"

    def actualizar_datos(self, nombre=None, apellido=None, telefono=None):
        if nombre is not None:
            self.__nombre = validar_texto(nombre, "nombre")
        if apellido is not None:
            self.__apellido = validar_texto(apellido, "apellido")
        if telefono is not None:
            self.__telefono = validar_telefono(telefono)

    def consultar_paciente(self):
        return f"{self.__id_paciente} | {self.__nombre} {self.__apellido} | DNI {self.dni_enmascarado}"

    def agregar_atencion(self, atencion):
        self.__atenciones.append(atencion)

    def get_atenciones(self):
        return tuple(self.__atenciones)
