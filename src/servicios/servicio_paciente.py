from src.modelos.gestor_sistema import GestorSistema
from src.modelos.paciente import Paciente
from src.utils.excepciones import RegistroDuplicadoError, RegistroNoEncontradoError
from src.utils.validaciones import validar_dni


class ServicioPaciente:
    def __init__(self):
        self.__pacientes = []

    def registrar_paciente(self, id_paciente, nombre, apellido, dni, telefono):
        paciente = Paciente(id_paciente, nombre, apellido, dni, telefono)
        if any(p.dni == paciente.dni for p in self.__pacientes):
            raise RegistroDuplicadoError("Ya existe un paciente con ese DNI.")
        self.__pacientes.append(paciente)
        GestorSistema.obtener_instancia().emitir(
            "paciente_registrado", id_paciente=paciente.id_paciente
        )
        return paciente

    def buscar_por_dni(self, dni):
        validar_dni(dni)
        for paciente in self.__pacientes:
            if paciente.dni == dni:
                return paciente
        raise RegistroNoEncontradoError("No se encontró un paciente con ese DNI.")

    def actualizar_paciente(self, dni, **datos):
        self.buscar_por_dni(dni).actualizar_datos(**datos)

    def listar_pacientes(self):
        return list(self.__pacientes)

    def obtener_resumen_pacientes(self):
        # map(): transforma cada Paciente en un texto sin mostrar el DNI completo
        return list(map(lambda p: p.consultar_paciente(), self.__pacientes))
