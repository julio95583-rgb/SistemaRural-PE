from src.modelos.gestor_sistema import GestorSistema
from src.utils.excepciones import PermisoDenegadoError


class ServicioReporte:
    def generar_reporte(self, usuario, tipo, datos, fecha_inicio, fecha_fin):
        if not usuario.verificar_permisos("generar_reportes"):
            raise PermisoDenegadoError("El usuario no puede generar reportes.")
        if str(tipo).lower() in ("citas", "atenciones"):
            # filter(): se conservan solo los elementos dentro del rango de fechas
            datos = list(filter(lambda d: fecha_inicio <= d.fecha <= fecha_fin, datos))
        return GestorSistema.obtener_instancia().crear_reporte(
            tipo, fecha_inicio, fecha_fin, datos
        )
