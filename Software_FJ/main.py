"""Punto de entrada y demostración de operaciones del sistema Software FJ."""

from clientes import Cliente

from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

from sistema import SistemaGestion

from excepciones import (
    ErrorSoftwareFJ,
    ReservaError
)

from registro_logs import logger


def ejecutar_demo():

    sistema = SistemaGestion()

    print("\n========== SOFTWARE FJ | SISTEMA DE GESTIÓN ==========")

    # OPERACIÓN 1: Registro válido de cliente.

    try:

        cliente = sistema.registrar_cliente(
            Cliente(
                "C001",
                "Ana Pérez",
                "ana@email.com",
                "3001234567"
            )
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 1: %s", error)

    else:

        print(
            "1. Cliente válido registrado:",
            cliente.nombre
        )

    # OPERACIÓN 2: Registro inválido de cliente.

    try:

        sistema.registrar_cliente(
            Cliente(
                "C002",
                "Luis Gómez",
                "correo-invalido",
                "3001234568"
            )
        )

    except ErrorSoftwareFJ as error:

        logger.warning(
            "2. Registro inválido controlado: %s",
            error
        )

        print(
            "2. Cliente inválido rechazado correctamente."
        )

    # OPERACIÓN 3: Segundo cliente válido.

    try:

        sistema.registrar_cliente(
            Cliente(
                "C003",
                "Carlos Ruiz",
                "carlos@email.com",
                "3105556677"
            )
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 3: %s", error)

    else:

        print(
            "3. Segundo cliente registrado correctamente."
        )

    # OPERACIÓN 4: Creación correcta de sala.

    try:

        sala = sistema.agregar_servicio(
            ServicioSala(
                "S001",
                "Sala Ejecutiva",
                50000,
                12
            )
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 4: %s", error)

    else:

        print(
            "4. Servicio creado:",
            sala.describir()
        )

    # OPERACIÓN 5: Creación correcta de alquiler de equipo.

    try:

        equipo = sistema.agregar_servicio(
            ServicioEquipo(
                "S002",
                "Video beam",
                20000,
                5
            )
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 5: %s", error)

    else:

        print(
            "5. Servicio creado:",
            equipo.describir()
        )

    # OPERACIÓN 6: Creación correcta de asesoría.

    try:

        asesoria = sistema.agregar_servicio(
            ServicioAsesoria(
                "S003",
                "Asesoría tecnológica",
                80000,
                "Tecnología"
            )
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 6: %s", error)

    else:

        print(
            "6. Servicio creado:",
            asesoria.describir()
        )

    # OPERACIÓN 7: Creación incorrecta de servicio.

    try:

        sistema.agregar_servicio(
            ServicioSala(
                "S004",
                "Sala inválida",
                -1000,
                10
            )
        )

    except ErrorSoftwareFJ as error:

        logger.warning(
            "7. Servicio inválido rechazado: %s",
            error
        )

        print(
            "7. Servicio con precio inválido rechazado correctamente."
        )

    # OPERACIÓN 8: Reserva de sala exitosa.

    try:

        reserva1 = sistema.crear_reserva(
            "R001",
            "C001",
            "S001",
            2,
            {"personas": 8}
        )

        reserva1.confirmar()

        total1 = reserva1.procesar(
            impuesto=0.19
        )

        print(
            f"8. Reserva de sala procesada. Total: ${total1:,.2f}"
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 8: %s", error)

    # OPERACIÓN 9: Reserva de equipo exitosa con descuento.

    try:

        reserva2 = sistema.crear_reserva(
            "R002",
            "C003",
            "S002",
            3,
            {"cantidad": 2}
        )

        reserva2.confirmar()

        total2 = reserva2.procesar(
            descuento=0.10
        )

        print(
            f"9. Reserva de equipo procesada. Total: ${total2:,.2f}"
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 9: %s", error)

    # OPERACIÓN 10: Reserva de asesoría exitosa.

    try:

        reserva3 = sistema.crear_reserva(
            "R003",
            "C001",
            "S003",
            2
        )

        reserva3.confirmar()

        total3 = reserva3.procesar(
            impuesto=0.19,
            descuento=0.05
        )

        print(
            f"10. Reserva de asesoría procesada. Total: ${total3:,.2f}"
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 10: %s", error)

    # OPERACIÓN 11: Reserva fallida por exceder capacidad.

    try:

        reserva4 = sistema.crear_reserva(
            "R004",
            "C001",
            "S001",
            2,
            {"personas": 30}
        )

        reserva4.confirmar()

    except ErrorSoftwareFJ as error:

        logger.warning(
            "11. Reserva fallida controlada: %s",
            error
        )

        print(
            "11. Reserva con capacidad excedida rechazada correctamente."
        )

    # OPERACIÓN 12: Servicio no disponible.

    try:

        equipo.disponible = False

        reserva5 = sistema.crear_reserva(
            "R005",
            "C003",
            "S002",
            1,
            {"cantidad": 1}
        )

        reserva5.confirmar()

    except ErrorSoftwareFJ as error:

        logger.warning(
            "12. Servicio no disponible controlado: %s",
            error
        )

        print(
            "12. Reserva de servicio no disponible rechazada correctamente."
        )

    # OPERACIÓN 13: Cancelación de reserva pendiente.

    try:

        reserva6 = sistema.crear_reserva(
            "R006",
            "C001",
            "S003",
            1
        )

        reserva6.cancelar()

        print(
            "13. Cancelación realizada:",
            reserva6.estado
        )

    except ErrorSoftwareFJ as error:

        logger.error("Operación 13: %s", error)

    # OPERACIÓN 14: Búsqueda de cliente inexistente.

    try:

        sistema.buscar_cliente("C999")

    except ErrorSoftwareFJ as error:

        logger.warning(
            "14. Búsqueda controlada: %s",
            error
        )

        print(
            "14. Búsqueda de cliente inexistente controlada."
        )

    # MECANISMO try/except/else.

    try:

        costo = sala.calcular_costo(
            1,
            personas=2
        )

    except ErrorSoftwareFJ as error:

        logger.error(
            "Cálculo alternativo fallido: %s",
            error
        )

    else:

        print(
            f"15. Cálculo sin impuesto ni descuento: ${costo:,.2f}"
        )

    # MECANISMO try/except/finally.

    try:

        print(
            "16. Verificación de estado:",
            len(sistema.reservas),
            "reservas creadas."
        )

    except Exception as error:

        logger.exception(
            "Error en verificación de estado: %s",
            error
        )

    finally:

        print(
            "16. Bloque finally ejecutado: verificación finalizada."
        )

    # ENCADENAMIENTO DE EXCEPCIONES.

    try:

        try:

            int("dato-no-numerico")

        except ValueError as error_original:

            raise ReservaError(
                "Error de conversión durante una operación de reserva."
            ) from error_original

    except ReservaError as error:

        logger.exception(
            "17. Ejemplo de encadenamiento de excepciones: %s",
            error
        )

        print(
            "17. Encadenamiento de excepciones demostrado y registrado."
        )

    print("\n========== RESUMEN ==========")

    print(
        f"Clientes registrados: {len(sistema.clientes)}"
    )

    print(
        f"Servicios registrados: {len(sistema.servicios)}"
    )

    print(
        f"Reservas creadas: {len(sistema.reservas)}"
    )

    print(
        "Los eventos y errores se registraron en logs/sistema.log."
    )

    print(
        "La demostración terminó sin detenerse por los errores controlados."
    )


if __name__ == "__main__":

    ejecutar_demo()