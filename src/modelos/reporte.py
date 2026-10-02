from abc import ABC, abstractmethod


class Reporte(ABC):
    def __init__(self, tipo_reporte, fecha_inicio, fecha_fin, datos):
        self.__tipo_reporte = tipo_reporte
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__datos = list(datos)

    @property
    def tipo_reporte(self):
        return self.__tipo_reporte

    @property
    def fecha_inicio(self):
        return self.__fecha_inicio

    @property
    def fecha_fin(self):
        return self.__fecha_fin

    @abstractmethod
    def _formatear_linea(self, elemento):
        """Cada tipo de reporte define cómo se muestra un elemento."""

    @abstractmethod
    def generar_reporte(self):
        """Devuelve el contenido del reporte como texto."""

    def _construir_texto(self, titulo):
        # Programación funcional: map() transforma cada elemento en una línea.
        lineas = list(map(self._formatear_linea, self.__datos))
        encabezado = [titulo, f"Total de registros: {len(lineas)}"]
        return "\n".join(encabezado + lineas)

    def exportar_reporte(self, ruta):
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(self.generar_reporte())
