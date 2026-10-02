# Trazabilidad del proyecto

## Requerimientos y código

| Código | Requerimiento | Implementación |
|---|---|---|
| RF01 | Registro de pacientes | `ServicioPaciente.registrar_paciente()`, clase `Paciente` |
| RF02 | Consulta de pacientes | `buscar_por_dni()`, `listar_pacientes()`, `obtener_resumen_pacientes()` |
| RF03 | Actualización de pacientes | `ServicioPaciente.actualizar_paciente()`, `Paciente.actualizar_datos()` |
| RF04 | Gestión de citas | `ServicioCita.registrar_cita()`, `cancelar_cita()`, `Cita.confirmar_cita()` |
| RF05 | Registro de atenciones | `ServicioAtencion.registrar_atencion()`, clase `Atencion` |
| RF06 | Generación de reportes | `ServicioReporte.generar_reporte()`, `ReporteFactory`, subclases de `Reporte` |
| RF07 | Filtrado de información | `ServicioCita.filtrar_por_estado()` (usa `filter()`) |
| RF08 | Validación y manejo de errores | `utils/validaciones.py`, `utils/excepciones.py` |

## Decisiones de diseño

| ID | Decisión | Código |
|---|---|---|
| DD-01 | POO como paradigma principal | `src/modelos/` |
| DD-02 | Singleton | `gestor_sistema.py` |
| DD-03 | Factory | `reporte_factory.py` |
| DD-04 | Encapsular atributos | Atributos privados y propiedades |
| DD-05 | Utilizar `filter()` | `servicio_cita.py` |
| DD-06 | Utilizar `map()` | `reporte.py`, `servicio_paciente.py` |
| DD-07 | Separar roles de usuario | `verificar_permisos()` |
| DD-08 | Utilizar excepciones | `excepciones.py`, `validaciones.py` |
| DD-09 | Programación orientada a eventos | `suscribir()` y `emitir()` en `GestorSistema` |
| DD-10 | Hash de contraseña y DNI enmascarado | `usuario.py`, `enmascarar_dni()` |
