# Software FJ

## Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto académico del curso Programación (213023),
UNAD – Fase 4.

## Objetivo

Construir una aplicación de consola en Python,
orientada a objetos, para administrar clientes,
servicios y reservas sin utilizar bases de datos.

## Requisitos

- Python 3.10 o superior.
- Se recomienda Python 3.12.
- No requiere instalar paquetes externos.

## Estructura

- main.py: ejecución de la demostración.
- entidades.py: clase abstracta Entidad.
- clientes.py: clase Cliente y validaciones.
- servicios.py: clase abstracta Servicio y servicios especializados.
- reservas.py: ciclo de vida de las reservas.
- sistema.py: listas y operaciones de gestión.
- excepciones.py: excepciones personalizadas.
- registro_logs.py: registro de eventos y errores.
- pruebas.py: pruebas automatizadas.
- logs/sistema.log: archivo generado al ejecutar el programa.

## Cómo ejecutar

1. Descargar y descomprimir el proyecto.
2. Abrir una terminal dentro de la carpeta Software_FJ.
3. Ejecutar:

python main.py

4. Para ejecutar las pruebas:

python -m unittest -v pruebas.py

En algunos equipos Windows se puede utilizar:

py main.py

py -m unittest -v pruebas.py

## Funcionalidades

- Registro y validación de clientes.
- Gestión de salas, equipos y asesorías.
- Creación y procesamiento de reservas.
- Confirmación y cancelación.
- Cálculo de costos con impuestos y descuentos.
- Excepciones personalizadas.
- Registro de errores y eventos.
- Gestión mediante objetos y listas.
- Sin utilización de bases de datos.

## Manejo de excepciones

El proyecto demuestra:

- try/except.
- try/except/else.
- try/except/finally.
- Encadenamiento mediante raise ... from ...

Los eventos y errores se registran en logs/sistema.log.

## Modalidad de desarrollo

Proyecto desarrollado individualmente como
actividad académica del curso Programación
de la UNAD.
