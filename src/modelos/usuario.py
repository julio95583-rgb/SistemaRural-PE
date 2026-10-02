import hashlib
import hmac
import os
from abc import ABC, abstractmethod

from src.utils.validaciones import validar_contrasena, validar_texto


class Usuario(ABC):
    _ITERACIONES = 100_000

    def __init__(self, id_usuario, nombre_usuario, contrasena, rol):
        self.__id_usuario = id_usuario
        self.__nombre_usuario = validar_texto(nombre_usuario, "nombre de usuario")
        self.__rol = validar_texto(rol, "rol")
        validar_contrasena(contrasena)
        # La contraseña no se guarda en texto plano: solo su hash con sal.
        self.__sal = os.urandom(16)
        self.__hash = self.__calcular_hash(contrasena)
        self.__sesion_activa = False

    def __calcular_hash(self, contrasena):
        return hashlib.pbkdf2_hmac(
            "sha256", contrasena.encode("utf-8"), self.__sal, self._ITERACIONES
        )

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def nombre_usuario(self):
        return self.__nombre_usuario

    @property
    def rol(self):
        return self.__rol

    @property
    def sesion_activa(self):
        return self.__sesion_activa

    def iniciar_sesion(self, contrasena):
        valido = hmac.compare_digest(self.__calcular_hash(str(contrasena)), self.__hash)
        self.__sesion_activa = valido
        return valido

    def cerrar_sesion(self):
        self.__sesion_activa = False

    @abstractmethod
    def verificar_permisos(self, accion):
        """Cada rol define qué acciones puede realizar."""
