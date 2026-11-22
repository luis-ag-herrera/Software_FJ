"""Coordinador del sistema: administra objetos mediante listas en memoria."""

from excepciones import (
    ValidacionError,
    ClienteNoEncontradoError
)

from registro_logs import logger


class SistemaGestion:

    def __init__(self):

        self.clientes = []

        self.servicios = []

        self.reservas = []

    def registrar_cliente(self, cliente):

        if any(
            c.identificador == cliente.identificador
            for c in self.clientes
        ):

            raise ValidacionError(
                "Ya existe un cliente con ese identificador."
            )

        self.clientes.append(cliente)

        logger.info(
            "Cliente registrado: %s.",
            cliente.identificador
        )

        return cliente

    def buscar_cliente(self, identificador):

        for cliente in self.clientes:

            if cliente.identificador == identificador:

                return cliente

        raise ClienteNoEncontradoError(
            f"No existe el cliente {identificador}."
        )

    def agregar_servicio(self, servicio):

        if any(
            s.identificador == servicio.identificador
            for s in self.servicios
        ):

            raise ValidacionError(
                "Ya existe un servicio con ese identificador."
            )

        self.servicios.append(servicio)

        logger.info(
            "Servicio agregado: %s.",
            servicio.identificador
        )

        return servicio

    def buscar_servicio(self, identificador):

        for servicio in self.servicios:

            if servicio.identificador == identificador:

                return servicio

        raise ValidacionError(
            f"No existe el servicio {identificador}."
        )

    def crear_reserva(
        self,
        identificador,
        cliente_id,
        servicio_id,
        duracion,
        parametros=None
    ):

        from reservas import Reserva

        cliente = self.buscar_cliente(cliente_id)

        servicio = self.buscar_servicio(servicio_id)

        if any(
            r.identificador == identificador
            for r in self.reservas
        ):

            raise ValidacionError(
                "Ya existe una reserva con ese identificador."
            )

        reserva = Reserva(
            identificador,
            cliente,
            servicio,
            duracion,
            parametros
        )

        self.reservas.append(reserva)

        logger.info(
            "Reserva creada: %s.",
            identificador
        )

        return reserva