from datetime import date

from src.modelos.administrador import Administrador
from src.modelos.gestor_sistema import GestorSistema
from src.modelos.personal_salud import PersonalSalud
from src.servicios.servicio_atencion import ServicioAtencion
from src.servicios.servicio_cita import ServicioCita
from src.servicios.servicio_paciente import ServicioPaciente
from src.servicios.servicio_reporte import ServicioReporte
from src.utils.excepciones import SistemaRuralError


def main():
    gestor = GestorSistema.obtener_instancia()
    # Programación orientada a eventos: el sistema reacciona a acciones del usuario
    gestor.suscribir("paciente_registrado", lambda id_paciente: print(f"[EVENTO] Paciente {id_paciente} registrado"))
    gestor.suscribir("cita_registrada", lambda id_cita: print(f"[EVENTO] Cita {id_cita} registrada"))
    gestor.iniciar_sistema()

    servicio_paciente = ServicioPaciente()
    servicio_cita = ServicioCita()
    servicio_atencion = ServicioAtencion()
    servicio_reporte = ServicioReporte()

    # Todos los datos son ficticios (restricción R05)
    admin = Administrador(1, "admin_demo", "clave-demo-123")
    medico = PersonalSalud(2, "medico_demo", "clave-demo-456", "Medicina general")
    admin.iniciar_sesion("clave-demo-123")
    medico.iniciar_sesion("clave-demo-456")
    admin.gestionar_usuarios(gestor, medico)

    p1 = medico.registrar_paciente(servicio_paciente, 1, "Ana", "Prueba", "00000001", "900000001")
    p2 = medico.registrar_paciente(servicio_paciente, 2, "Luis", "Ejemplo", "00000002", "900000002")
    print(p1.registrar_paciente())

    medico.gestionar_cita(servicio_cita, 1, date(2026, 10, 5), "09:00", p1)
    medico.gestionar_cita(servicio_cita, 2, date(2026, 10, 6), "10:30", p2)
    servicio_cita.cancelar_cita(2)
    medico.registrar_atencion(servicio_atencion, 1, date(2026, 10, 5), "Control general", "Sin novedades", p1)

    print("Citas pendientes:", [c.id_cita for c in servicio_cita.listar_citas_pendientes()])
    print("Resumen de pacientes:", servicio_paciente.obtener_resumen_pacientes())

    reporte = admin.generar_reportes(
        servicio_reporte, "citas", servicio_cita.listar_citas(),
        date(2026, 10, 1), date(2026, 10, 31),
    )
    print(reporte.generar_reporte())

    try:
        medico.registrar_paciente(servicio_paciente, 3, "Eva", "Error", "123", "900000003")
    except SistemaRuralError as error:
        print(f"[ERROR CONTROLADO] {error}")

    gestor.cerrar_sistema()


if __name__ == "__main__":
    main()
