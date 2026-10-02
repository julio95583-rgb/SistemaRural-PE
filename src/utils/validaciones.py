import re
from datetime import date

from src.utils.excepciones import ValidacionError

ESTADOS_CITA = ("PENDIENTE", "CONFIRMADA", "ATENDIDA", "CANCELADA")


def validar_texto(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValidacionError(f"El campo '{campo}' no puede estar vacío.")
    return valor.strip()


def validar_dni(dni):
    if not isinstance(dni, str) or not re.fullmatch(r"\d{8}", dni):
        raise ValidacionError("El DNI debe tener exactamente 8 dígitos numéricos.")
    return dni


def validar_telefono(telefono):
    if not isinstance(telefono, str) or not re.fullmatch(r"\d{9}", telefono):
        raise ValidacionError("El teléfono debe tener 9 dígitos numéricos.")
    return telefono


def validar_contrasena(contrasena):
    if not isinstance(contrasena, str) or len(contrasena) < 8:
        raise ValidacionError("La contraseña debe tener al menos 8 caracteres.")
    return contrasena


def validar_fecha(fecha):
    if not isinstance(fecha, date):
        raise ValidacionError("La fecha debe ser un objeto de tipo date.")
    return fecha


def validar_hora(hora):
    if not isinstance(hora, str) or not re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", hora):
        raise ValidacionError("La hora debe tener el formato HH:MM.")
    return hora


def validar_estado_cita(estado):
    if not isinstance(estado, str) or estado.upper() not in ESTADOS_CITA:
        raise ValidacionError(f"Estado de cita no válido. Use: {', '.join(ESTADOS_CITA)}.")
    return estado.upper()


def enmascarar_dni(dni):
    """Oculta los primeros dígitos del DNI para mostrarlo en pantalla o reportes."""
    return "*" * 5 + dni[-3:]
