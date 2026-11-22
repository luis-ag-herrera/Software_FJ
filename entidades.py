"""Entidad abstracta común para los objetos principales del sistema."""

from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificador: str, nombre: str):

        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador es obligatorio.")

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        self._identificador = identificador.strip()
        self._nombre = nombre.strip()

    @property
    def identificador(self) -> str:
        return self._identificador

    @property
    def nombre(self) -> str:
        return self._nombre

    @abstractmethod
    def describir(self) -> str:
        """Devuelve una descripción legible de la entidad."""