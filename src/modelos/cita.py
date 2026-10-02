from src.utils.excepciones import ValidacionError
from src.utils.validaciones import validar_estado_cita, validar_fecha, validar_hora


class Cita:
    def __init__(self, id_cita, fecha, hora, paciente, personal_salud=None):
        self.__id_cita = id_cita
        self.__fecha = validar_fecha(fecha)
        self.__hora = validar_hora(hora)
        self.__estado = "PENDIENTE"
        self.__paciente = paciente              # Asociación Paciente 1 — 0..* Cita
        self.__personal_salud = personal_salud  # Agregación PersonalSalud 1 ◇— 0..* Cita

    @property
    def id_cita(self):
        return self.__id_cita

    @property
    def fecha(self):
        return self.__fecha

    @property
    def hora(self):
        return self.__hora

    @property
    def estado(self):
        return self.__estado

    @property
    def paciente(self):
        return self.__paciente

    @property
    def personal_salud(self):
        return self.__personal_salud

    def registrar_cita(self):
        return f"Cita {self.__id_cita} registrada para {self.__paciente.get_nombre()}"

    def confirmar_cita(self):
        if self.__estado != "PENDIENTE":
            raise ValidacionError("Solo se puede confirmar una cita pendiente.")
        self.__estado = validar_estado_cita("CONFIRMADA")

    def cancelar_cita(self):
        if self.__estado == "ATENDIDA":
            raise ValidacionError("No se puede cancelar una cita ya atendida.")
        self.__estado = validar_estado_cita("CANCELADA")

    def consultar_cita(self):
        return (f"{self.__id_cita} | {self.__fecha.isoformat()} {self.__hora} | "
                f"{self.__estado} | {self.__paciente.get_nombre()}")
