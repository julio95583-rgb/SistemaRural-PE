from src.modelos.usuario import Usuario
from src.utils.excepciones import PermisoDenegadoError
from src.utils.validaciones import validar_texto


class PersonalSalud(Usuario):
    _PERMISOS = ("registrar_paciente", "gestionar_cita", "registrar_atencion", "consultar")

    def __init__(self, id_usuario, nombre_usuario, contrasena, especialidad):
        super().__init__(id_usuario, nombre_usuario, contrasena, "PERSONAL_SALUD")
        self.__especialidad = validar_texto(especialidad, "especialidad")

    @property
    def especialidad(self):
        return self.__especialidad

    def verificar_permisos(self, accion):
        return self.sesion_activa and accion in self._PERMISOS

    def _exigir(self, accion):
        if not self.verificar_permisos(accion):
            raise PermisoDenegadoError(f"No tiene permiso para: {accion}.")

    def registrar_paciente(self, servicio_paciente, id_paciente, nombre, apellido, dni, telefono):
        self._exigir("registrar_paciente")
        return servicio_paciente.registrar_paciente(id_paciente, nombre, apellido, dni, telefono)

    def gestionar_cita(self, servicio_cita, id_cita, fecha, hora, paciente):
        self._exigir("gestionar_cita")
        return servicio_cita.registrar_cita(id_cita, fecha, hora, paciente, self)

    def registrar_atencion(self, servicio_atencion, id_atencion, fecha, motivo, observacion, paciente):
        self._exigir("registrar_atencion")
        return servicio_atencion.registrar_atencion(id_atencion, fecha, motivo, observacion, paciente)
