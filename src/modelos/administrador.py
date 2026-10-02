from src.modelos.usuario import Usuario
from src.utils.excepciones import PermisoDenegadoError


class Administrador(Usuario):
    _PERMISOS = ("gestionar_usuarios", "generar_reportes", "consultar")

    def __init__(self, id_usuario, nombre_usuario, contrasena):
        super().__init__(id_usuario, nombre_usuario, contrasena, "ADMINISTRADOR")

    def verificar_permisos(self, accion):
        return self.sesion_activa and accion in self._PERMISOS

    def gestionar_usuarios(self, gestor, usuario):
        if not self.verificar_permisos("gestionar_usuarios"):
            raise PermisoDenegadoError("No tiene permiso para gestionar usuarios.")
        gestor.registrar_usuario(usuario)

    def generar_reportes(self, servicio_reporte, tipo, datos, fecha_inicio, fecha_fin):
        return servicio_reporte.generar_reporte(self, tipo, datos, fecha_inicio, fecha_fin)
