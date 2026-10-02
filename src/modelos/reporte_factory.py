from src.modelos.reporte_concreto import ReporteAtenciones, ReporteCitas, ReportePacientes
from src.utils.excepciones import ValidacionError


class ReporteFactory:
    _TIPOS = {
        "pacientes": ReportePacientes,
        "citas": ReporteCitas,
        "atenciones": ReporteAtenciones,
    }

    @staticmethod
    def crear_reporte(tipo, fecha_inicio, fecha_fin, datos):
        clase = ReporteFactory._TIPOS.get(str(tipo).lower())
        if clase is None:
            raise ValidacionError(f"Tipo de reporte no válido: {tipo}")
        return clase(fecha_inicio, fecha_fin, datos)
