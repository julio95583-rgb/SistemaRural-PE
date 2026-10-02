# Tratamiento de datos personales

Los datos de salud son datos sensibles según la Ley N.º 29733, Ley de Protección de Datos Personales, y su reglamento (Decreto Supremo N.º 016-2024-JUS).

## Medidas aplicadas en el prototipo

- Todos los datos de prueba son ficticios (restricción R05).
- Las contraseñas no se guardan en texto plano; se almacena su hash PBKDF2-HMAC-SHA256 con sal aleatoria.
- El DNI se valida (8 dígitos) y se muestra enmascarado en pantalla y reportes.
- Solo pueden operar usuarios con sesión iniciada y permiso para la acción.
- Los atributos son privados y las colecciones se devuelven como copia o tupla.

## Limitaciones

- Los datos se guardan solo en memoria; no hay base de datos ni cifrado de almacenamiento.
- Una puesta en producción requeriría cifrado, respaldos, registro de accesos y las demás medidas de seguridad que exige la normativa.
