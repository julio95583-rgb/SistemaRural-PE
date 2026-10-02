from datetime import date

from src.servicios.servicio_cita import ServicioCita
from src.servicios.servicio_paciente import ServicioPaciente


def test_filtrado_de_citas_pendientes_con_filter():
    pacientes = ServicioPaciente()
    citas = ServicioCita()
    paciente = pacientes.registrar_paciente(1, "Ana", "Prueba", "00000001", "900000001")
    citas.registrar_cita(1, date(2026, 10, 5), "09:00", paciente)
    citas.registrar_cita(2, date(2026, 10, 6), "10:00", paciente)
    citas.registrar_cita(3, date(2026, 10, 7), "11:00", paciente)
    citas.cancelar_cita(2)
    pendientes = citas.listar_citas_pendientes()
    assert [c.id_cita for c in pendientes] == [1, 3]
