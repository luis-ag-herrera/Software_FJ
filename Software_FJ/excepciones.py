"""Excepciones propias del sistema Software FJ."""


class ErrorSoftwareFJ(Exception):
    """Excepción base para los errores controlados del sistema."""


class ValidacionError(ErrorSoftwareFJ):
    """Se utiliza cuando un dato no cumple las reglas de validación."""


class ClienteNoEncontradoError(ErrorSoftwareFJ):
    """Se utiliza cuando un cliente no está registrado."""


class ServicioNoDisponibleError(ErrorSoftwareFJ):
    """Se utiliza cuando un servicio no está disponible."""


class ReservaError(ErrorSoftwareFJ):
    """Se utiliza cuando una reserva no puede procesarse."""


class OperacionNoPermitidaError(ErrorSoftwareFJ):
    """Se utiliza cuando se intenta una operación incompatible con el estado."""