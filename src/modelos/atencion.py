from src.utils.validaciones import validar_fecha, validar_texto


class Atencion:
    def __init__(self, id_atencion, fecha, motivo, observacion, paciente):
        self.__id_atencion = id_atencion
        self.__fecha = validar_fecha(fecha)
        self.__motivo = validar_texto(motivo, "motivo")
        self.__observacion = validar_texto(observacion, "observación")
        self.__paciente = paciente  # Composición con Paciente

    @property
    def id_atencion(self):
        return self.__id_atencion

    @property
    def fecha(self):
        return self.__fecha

    @property
    def motivo(self):
        return self.__motivo

    @property
    def paciente(self):
        return self.__paciente

    def registrar_atencion(self):
        self.__paciente.agregar_atencion(self)

    def actualizar_atencion(self, motivo=None, observacion=None):
        if motivo is not None:
            self.__motivo = validar_texto(motivo, "motivo")
        if observacion is not None:
            self.__observacion = validar_texto(observacion, "observación")

    def generar_resumen(self):
        return f"{self.__id_atencion} | {self.__fecha.isoformat()} | {self.__motivo}"
