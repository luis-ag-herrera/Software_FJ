"""Entidad Reserva y ciclo de vida de una reserva."""

from entidades import Entidad

from excepciones import (
    ReservaError,
    OperacionNoPermitidaError
)

from registro_logs import logger


class Reserva(Entidad):

    ESTADOS_VALIDOS = {
        "Pendiente",
        "Confirmada",
        "Cancelada",
        "Procesada"
    }

    def __init__(
        self,
        identificador,
        cliente,
        servicio,
        duracion,
        parametros=None
    ):

        super().__init__(
            identificador,
            f"Reserva {identificador}"
        )

        if cliente is None or servicio is None:

            raise ReservaError(
                "La reserva requiere un cliente y un servicio."
            )

        self.cliente = cliente

        self.servicio = servicio

        self.duracion = duracion

        self.parametros = parametros or {}

        self.estado = "Pendiente"

        self.total = None

    def confirmar(self):

        if self.estado != "Pendiente":

            raise OperacionNoPermitidaError(
                "Solo se puede confirmar una reserva pendiente."
            )

        self.servicio.validar_parametros(
            self.duracion,
            **self.parametros
        )

        self.estado = "Confirmada"

        logger.info(
            "Reserva %s confirmada para cliente %s.",
            self.identificador,
            self.cliente.identificador
        )

        return self.estado

    def cancelar(self):

        if self.estado not in {"Pendiente", "Confirmada"}:

            raise OperacionNoPermitidaError(
                "No se puede cancelar una reserva procesada o ya cancelada."
            )

        self.estado = "Cancelada"

        logger.info(
            "Reserva %s cancelada.",
            self.identificador
        )

        return self.estado

    def procesar(self, impuesto=0.0, descuento=0.0):

        if self.estado != "Confirmada":

            raise OperacionNoPermitidaError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        try:

            self.total = self.servicio.calcular_costo(
                self.duracion,
                impuesto,
                descuento,
                **self.parametros
            )

            self.estado = "Procesada"

            logger.info(
                "Reserva %s procesada. Total: $%.2f",
                self.identificador,
                self.total
            )

            return self.total

        except Exception as error:

            logger.exception(
                "Error al procesar reserva %s.",
                self.identificador
            )

            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

    def describir(self):

        return (
            f"{self.identificador} | "
            f"{self.cliente.nombre} | "
            f"{self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )

    def __str__(self):

        return self.describir()