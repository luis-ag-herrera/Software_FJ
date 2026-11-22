"""Configuración centralizada del registro de eventos y errores."""

import logging
from pathlib import Path


RUTA_LOGS = Path(__file__).resolve().parent / "logs"

RUTA_LOGS.mkdir(exist_ok=True)

RUTA_ARCHIVO = RUTA_LOGS / "sistema.log"


def obtener_logger(nombre: str = "SoftwareFJ") -> logging.Logger:

    logger = logging.getLogger(nombre)

    logger.setLevel(logging.INFO)

    if not logger.handlers:

        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        archivo = logging.FileHandler(
            RUTA_ARCHIVO,
            encoding="utf-8"
        )

        archivo.setFormatter(formato)

        consola = logging.StreamHandler()

        consola.setFormatter(formato)

        logger.addHandler(archivo)

        logger.addHandler(consola)

    return logger


logger = obtener_logger()