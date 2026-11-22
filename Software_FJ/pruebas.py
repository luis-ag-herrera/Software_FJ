"""Pruebas automatizadas básicas del sistema Software FJ."""

import unittest

from clientes import Cliente

from servicios import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

from sistema import SistemaGestion

from excepciones import (
    ValidacionError,
    ServicioNoDisponibleError,
    OperacionNoPermitidaError
)


class PruebasSoftwareFJ(unittest.TestCase):

    def setUp(self):

        self.sistema = SistemaGestion()

        self.cliente = self.sistema.registrar_cliente(
            Cliente(
                "C100",
                "María López",
                "maria@email.com",
                "3001234567"
            )
        )

        self.sala = self.sistema.agregar_servicio(
            ServicioSala(
                "S100",
                "Sala de prueba",
                50000,
                10
            )
        )

    def test_registro_cliente_valido(self):

        self.assertEqual(
            self.cliente.nombre,
            "María López"
        )

    def test_correo_invalido(self):

        with self.assertRaises(ValidacionError):

            Cliente(
                "C101",
                "Pedro",
                "correo-mal",
                "3001234567"
            )

    def test_calculo_sala(self):

        self.assertEqual(
            self.sala.calcular_costo(
                2,
                personas=5
            ),
            100000.00
        )

    def test_calculo_con_impuesto_y_descuento(self):

        self.assertEqual(
            self.sala.calcular_costo(
                2,
                impuesto=0.19,
                descuento=0.10,
                personas=5
            ),
            107100.00
        )

    def test_reserva_procesada(self):

        reserva = self.sistema.crear_reserva(
            "R100",
            "C100",
            "S100",
            2,
            {"personas": 5}
        )

        reserva.confirmar()

        self.assertEqual(
            reserva.procesar(),
            100000.00
        )

        self.assertEqual(
            reserva.estado,
            "Procesada"
        )

    def test_capacidad_excedida(self):

        reserva = self.sistema.crear_reserva(
            "R101",
            "C100",
            "S100",
            2,
            {"personas": 20}
        )

        with self.assertRaises(ValidacionError):

            reserva.confirmar()

    def test_servicio_no_disponible(self):

        self.sala.disponible = False

        with self.assertRaises(ServicioNoDisponibleError):

            self.sala.calcular_costo(
                1,
                personas=2
            )

    def test_no_procesar_sin_confirmar(self):

        reserva = self.sistema.crear_reserva(
            "R102",
            "C100",
            "S100",
            1,
            {"personas": 2}
        )

        with self.assertRaises(OperacionNoPermitidaError):

            reserva.procesar()

    def test_tres_tipos_de_servicio(self):

        equipo = ServicioEquipo(
            "S101",
            "Portátil",
            10000,
            4
        )

        asesoria = ServicioAsesoria(
            "S102",
            "Asesoría",
            60000,
            "Sistemas"
        )

        self.assertEqual(
            equipo.calcular_costo(
                2,
                cantidad=2
            ),
            40000.00
        )

        self.assertEqual(
            asesoria.calcular_costo(2),
            120000.00
        )


if __name__ == "__main__":

    unittest.main(verbosity=2)