import pytest

from src.servicios.servicio_paciente import ServicioPaciente
from src.utils.excepciones import ValidacionError


def test_registro_exitoso_de_paciente_ficticio():
    servicio = ServicioPaciente()
    paciente = servicio.registrar_paciente(1, "Ana", "Prueba", "00000001", "900000001")
    assert servicio.buscar_por_dni("00000001") is paciente
    assert paciente.get_nombre() == "Ana"


def test_rechazo_de_dni_con_longitud_incorrecta():
    servicio = ServicioPaciente()
    with pytest.raises(ValidacionError):
        servicio.registrar_paciente(1, "Ana", "Prueba", "1234", "900000001")
