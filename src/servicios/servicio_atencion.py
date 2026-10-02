from src.modelos.atencion import Atencion
from src.modelos.gestor_sistema import GestorSistema


class ServicioAtencion:
    def __init__(self):
        self.__atenciones = []

    def registrar_atencion(self, id_atencion, fecha, motivo, observacion, paciente):
        atencion = Atencion(id_atencion, fecha, motivo, observacion, paciente)
        atencion.registrar_atencion()
        self.__atenciones.append(atencion)
        GestorSistema.obtener_instancia().emitir("atencion_registrada", id_atencion=id_atencion)
        return atencion

    def listar_atenciones(self):
        return list(self.__atenciones)
