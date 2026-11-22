"""Modelo Cliente con encapsulación y validaciones estrictas."""

import re

from entidades import Entidad
from excepciones import ValidacionError


class Cliente(Entidad):

    def __init__(
        self,
        identificador: str,
        nombre: str,
        correo: str,
        telefono: str
    ):

        super().__init__(identificador, nombre)

        self.correo = correo

        self.telefono = telefono

    @property
    def correo(self) -> str:

        return self._correo

    @correo.setter
    def correo(self, valor: str):

        if (
            not isinstance(valor, str)
            or not re.fullmatch(
                r"[^@\s]+@[^@\s]+\.[^@\s]+",
                valor.strip()
            )
        ):

            raise ValidacionError(
                "El correo electrónico no tiene un formato válido."
            )

        self._correo = valor.strip().lower()

    @property
    def telefono(self) -> str:

        return self._telefono

    @telefono.setter
    def telefono(self, valor: str):

        if not isinstance(valor, str):

            raise ValidacionError(
                "El teléfono debe ingresarse como texto."
            )

        limpio = re.sub(r"[\s()+-]", "", valor)

        if not limpio.isdigit() or not 7 <= len(limpio) <= 15:

            raise ValidacionError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        self._telefono = valor.strip()

    def describir(self) -> str:

        return (
            f"Cliente {self.nombre} | "
            f"ID: {self.identificador} | "
            f"Correo: {self.correo}"
        )

    def __str__(self):

        return self.describir()