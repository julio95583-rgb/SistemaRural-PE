from src.modelos.cita import Cita
from src.modelos.gestor_sistema import GestorSistema
from src.utils.excepciones import RegistroNoEncontradoError
from src.utils.validaciones import validar_estado_cita


class ServicioCita:
    def __init__(self):
        self.__citas = []

    def registrar_cita(self, id_cita, fecha, hora, paciente, personal_salud=None):
        cita = Cita(id_cita, fecha, hora, paciente, personal_salud)
        self.__citas.append(cita)
        GestorSistema.obtener_instancia().emitir("cita_registrada", id_cita=id_cita)
        return cita

    def buscar_cita(self, id_cita):
        for cita in self.__citas:
            if cita.id_cita == id_cita:
                return cita
        raise RegistroNoEncontradoError(f"No existe la cita {id_cita}.")

    def cancelar_cita(self, id_cita):
        cita = self.buscar_cita(id_cita)
        cita.cancelar_cita()
        GestorSistema.obtener_instancia().emitir("cita_cancelada", id_cita=id_cita)

    def listar_citas(self):
        return list(self.__citas)

    def filtrar_por_estado(self, estado):
        # filter(): selecciona las citas que cumplen la condición (RF07)
        estado = validar_estado_cita(estado)
        return list(filter(lambda c: c.estado == estado, self.__citas))

    def listar_citas_pendientes(self):
        return self.filtrar_por_estado("PENDIENTE")
