class SistemaRuralError(Exception):
    """Excepción base de SistemaRural-PE."""


class ValidacionError(SistemaRuralError):
    """Se lanza cuando un dato no cumple el formato esperado."""


class RegistroDuplicadoError(SistemaRuralError):
    """Se lanza cuando se intenta registrar un elemento que ya existe."""


class RegistroNoEncontradoError(SistemaRuralError):
    """Se lanza cuando no se encuentra el elemento buscado."""


class PermisoDenegadoError(SistemaRuralError):
    """Se lanza cuando el usuario no tiene permiso para la acción."""
