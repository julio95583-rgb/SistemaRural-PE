from src.modelos.reporte import Reporte


class ReportePacientes(Reporte):
    def __init__(self, fecha_inicio, fecha_fin, datos):
        super().__init__("pacientes", fecha_inicio, fecha_fin, datos)

    def _formatear_linea(self, paciente):
        return paciente.consultar_paciente()

    def generar_reporte(self):
        return self._construir_texto("REPORTE DE PACIENTES")


class ReporteCitas(Reporte):
    def __init__(self, fecha_inicio, fecha_fin, datos):
        super().__init__("citas", fecha_inicio, fecha_fin, datos)

    def _formatear_linea(self, cita):
        return cita.consultar_cita()

    def generar_reporte(self):
        return self._construir_texto("REPORTE DE CITAS")


class ReporteAtenciones(Reporte):
    def __init__(self, fecha_inicio, fecha_fin, datos):
        super().__init__("atenciones", fecha_inicio, fecha_fin, datos)

    def _formatear_linea(self, atencion):
        return f"{atencion.generar_resumen()} | {atencion.paciente.get_nombre()}"

    def generar_reporte(self):
        return self._construir_texto("REPORTE DE ATENCIONES")
