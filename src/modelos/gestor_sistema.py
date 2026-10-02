from src.modelos.reporte_factory import ReporteFactory


class GestorSistema:
    __instancia = None

    def __init__(self):
        if GestorSistema.__instancia is not None:
            raise RuntimeError("GestorSistema es Singleton: use obtener_instancia().")
        self.__configuracion = {
            "establecimiento": "Centro de Salud Rural Santa Rosa",
            "version": "1.0",
        }
        self.__usuarios = []
        self.__manejadores = {}  # evento -> lista de funciones
        self.__iniciado = False

    @classmethod
    def obtener_instancia(cls):
        if cls.__instancia is None:
            cls.__instancia = cls()
        return cls.__instancia

    @classmethod
    def reiniciar(cls):
        """Solo para pruebas: elimina la instancia para empezar con un estado limpio."""
        cls.__instancia = None

    def iniciar_sistema(self):
        self.__iniciado = True
        self.emitir("sistema_iniciado")

    def cerrar_sistema(self):
        self.emitir("sistema_cerrado")
        self.__iniciado = False

    @property
    def iniciado(self):
        return self.__iniciado

    def get_configuracion(self, clave):
        return self.__configuracion.get(clave)

    def set_configuracion(self, clave, valor):
        self.__configuracion[clave] = valor

    def registrar_usuario(self, usuario):
        self.__usuarios.append(usuario)
        self.emitir("usuario_registrado", usuario=usuario.nombre_usuario)

    def listar_usuarios(self):
        return tuple(self.__usuarios)

    def crear_reporte(self, tipo, fecha_inicio, fecha_fin, datos):
        return ReporteFactory.crear_reporte(tipo, fecha_inicio, fecha_fin, datos)

    # Programación orientada a eventos: suscripción y emisión de eventos
    def suscribir(self, evento, manejador):
        self.__manejadores.setdefault(evento, []).append(manejador)

    def emitir(self, evento, **datos):
        for manejador in self.__manejadores.get(evento, []):
            manejador(**datos)
