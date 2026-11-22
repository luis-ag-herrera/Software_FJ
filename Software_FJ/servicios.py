"""Servicios abstractos y especializados de Software FJ."""

from abc import abstractmethod

from entidades import Entidad

from excepciones import (
    ValidacionError,
    ServicioNoDisponibleError
)


class Servicio(Entidad):

    def __init__(
        self,
        identificador: str,
        nombre: str,
        precio_base: float,
        disponible: bool = True
    ):

        super().__init__(identificador, nombre)

        if (
            isinstance(precio_base, bool)
            or not isinstance(precio_base, (int, float))
            or precio_base <= 0
        ):

            raise ValidacionError(
                "El precio base debe ser un número positivo."
            )

        self._precio_base = float(precio_base)

        self._disponible = bool(disponible)

    @property
    def precio_base(self):

        return self._precio_base

    @property
    def disponible(self):

        return self._disponible

    @disponible.setter
    def disponible(self, valor):

        if not isinstance(valor, bool):

            raise ValidacionError(
                "La disponibilidad debe ser verdadera o falsa."
            )

        self._disponible = valor

    def validar_disponibilidad(self):

        if not self.disponible:

            raise ServicioNoDisponibleError(
                f"El servicio '{self.nombre}' no está disponible."
            )

    @abstractmethod
    def validar_parametros(self, duracion: int, **parametros):

        pass

    @abstractmethod
    def calcular_subtotal(self, duracion: int, **parametros) -> float:

        pass

    def calcular_costo(
        self,
        duracion: int,
        impuesto: float = 0.0,
        descuento: float = 0.0,
        **parametros
    ) -> float:

        """Calcula costos con parámetros opcionales."""

        self.validar_disponibilidad()

        self.validar_parametros(duracion, **parametros)

        if not 0 <= impuesto <= 1:

            raise ValidacionError(
                "El impuesto debe expresarse entre 0 y 1."
            )

        if not 0 <= descuento <= 1:

            raise ValidacionError(
                "El descuento debe expresarse entre 0 y 1."
            )

        subtotal = self.calcular_subtotal(
            duracion,
            **parametros
        )

        total = subtotal * (1 - descuento) * (1 + impuesto)

        if total < 0:

            raise ValidacionError(
                "El cálculo produjo un total inconsistente."
            )

        return round(total, 2)


# SERVICIO 1: RESERVA DE SALAS

class ServicioSala(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        precio_hora,
        capacidad_maxima,
        disponible=True
    ):

        super().__init__(
            identificador,
            nombre,
            precio_hora,
            disponible
        )

        if (
            isinstance(capacidad_maxima, bool)
            or not isinstance(capacidad_maxima, int)
            or capacidad_maxima <= 0
        ):

            raise ValidacionError(
                "La capacidad máxima debe ser un entero positivo."
            )

        self.capacidad_maxima = capacidad_maxima

    def validar_parametros(self, duracion, **parametros):

        self.validar_disponibilidad()

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):

            raise ValidacionError(
                "La duración de la sala debe ser un número entero de horas."
            )

        personas = parametros.get("personas")

        if (
            isinstance(personas, bool)
            or not isinstance(personas, int)
            or personas <= 0
        ):

            raise ValidacionError(
                "Debe indicar una cantidad positiva de personas."
            )

        if personas > self.capacidad_maxima:

            raise ValidacionError(
                "La cantidad de personas supera la capacidad de la sala."
            )

    def calcular_subtotal(self, duracion, **parametros):

        return self.precio_base * duracion

    def describir(self):

        return (
            f"Sala: {self.nombre} | "
            f"Capacidad: {self.capacidad_maxima} | "
            f"Precio/hora: ${self.precio_base:,.2f}"
        )


# SERVICIO 2: ALQUILER DE EQUIPOS

class ServicioEquipo(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        precio_hora,
        unidades_disponibles,
        disponible=True
    ):

        super().__init__(
            identificador,
            nombre,
            precio_hora,
            disponible
        )

        if (
            isinstance(unidades_disponibles, bool)
            or not isinstance(unidades_disponibles, int)
            or unidades_disponibles <= 0
        ):

            raise ValidacionError(
                "Las unidades disponibles deben ser un entero positivo."
            )

        self.unidades_disponibles = unidades_disponibles

    def validar_parametros(self, duracion, **parametros):

        self.validar_disponibilidad()

        cantidad = parametros.get("cantidad")

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):

            raise ValidacionError(
                "La duración del alquiler debe ser positiva."
            )

        if (
            isinstance(cantidad, bool)
            or not isinstance(cantidad, int)
            or cantidad <= 0
        ):

            raise ValidacionError(
                "La cantidad de equipos debe ser un entero positivo."
            )

        if cantidad > self.unidades_disponibles:

            raise ServicioNoDisponibleError(
                "No hay suficientes unidades del equipo solicitado."
            )

    def calcular_subtotal(self, duracion, **parametros):

        return (
            self.precio_base
            * duracion
            * parametros["cantidad"]
        )

    def describir(self):

        return (
            f"Equipo: {self.nombre} | "
            f"Unidades: {self.unidades_disponibles} | "
            f"Precio/hora: ${self.precio_base:,.2f}"
        )


# SERVICIO 3: ASESORÍAS ESPECIALIZADAS

class ServicioAsesoria(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        precio_sesion,
        especialidad,
        disponible=True
    ):

        super().__init__(
            identificador,
            nombre,
            precio_sesion,
            disponible
        )

        if (
            not isinstance(especialidad, str)
            or not especialidad.strip()
        ):

            raise ValidacionError(
                "La especialidad de la asesoría es obligatoria."
            )

        self.especialidad = especialidad.strip()

    def validar_parametros(self, duracion, **parametros):

        self.validar_disponibilidad()

        if (
            isinstance(duracion, bool)
            or not isinstance(duracion, int)
            or duracion <= 0
        ):

            raise ValidacionError(
                "La cantidad de sesiones debe ser un entero positivo."
            )

    def calcular_subtotal(self, duracion, **parametros):

        return self.precio_base * duracion

    def describir(self):

        return (
            f"Asesoría: {self.nombre} | "
            f"Especialidad: {self.especialidad} | "
            f"Precio/sesión: ${self.precio_base:,.2f}"
        )