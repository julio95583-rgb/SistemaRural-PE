# SistemaRural-PE

Prototipo en Python para digitalizar el registro de pacientes, citas y atenciones del Centro de Salud Rural "Santa Rosa" (Chugur, Cajamarca). Es un proyecto académico del curso Lenguajes de Programación (UPN).

## Paradigmas utilizados

- **Programación orientada a objetos:** clases con encapsulamiento, herencia, composición y agregación.
- **Programación funcional:** `filter()` y `map()` sobre las colecciones de pacientes, citas y reportes.
- **Programación orientada a eventos:** suscripción y emisión de eventos desde `GestorSistema`.

Patrones de diseño: Singleton (`GestorSistema`) y Factory (`ReporteFactory`).

## Requisitos

- Python 3.x
- pytest (`pip install -r requirements.txt`)

## Cómo ejecutar

Desde la carpeta raíz del proyecto:

```
python main.py
python -m pytest -v
```

## Estructura

```
main.py
requirements.txt
src/
  modelos/      clases del diagrama UML
  servicios/    lógica sobre pacientes, citas, atenciones y reportes
  utils/        validaciones y excepciones
tests/          pruebas automatizadas con pytest
docs/           documentación del proyecto
```

## Datos personales

Todos los datos de ejemplo son ficticios. Las contraseñas se guardan como hash y el DNI se muestra enmascarado en pantalla y reportes. Más detalle en `docs/datos_personales.md`.
