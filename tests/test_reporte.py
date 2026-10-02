import pytest

from src.modelos.reporte_concreto import ReportePacientes
from src.modelos.reporte_factory import ReporteFactory
from src.servicios.servicio_paciente import ServicioPaciente
from src.utils.excepciones import ValidacionError


def test_reporte_de_pacientes_no_muestra_dni_completo():
    servicio = ServicioPaciente()
    servicio.registrar_paciente(1, "Ana", "Prueba", "00000001", "900000001")
    reporte = ReporteFactory.crear_reporte("pacientes", None, None, servicio.listar_pacientes())
    texto = reporte.generar_reporte()
    assert isinstance(reporte, ReportePacientes)
    assert "00000001" not in texto
    assert "*****001" in texto


def test_factory_rechaza_tipo_de_reporte_invalido():
    with pytest.raises(ValidacionError):
        ReporteFactory.crear_reporte("medicamentos", None, None, [])
