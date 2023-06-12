from codigo import *
import unittest 
class TestSube(unittest.TestCase):
    def setUp(self):
        self.sube = Sube()
        self.sube.saldo = 1000

    def test_init(self):
        self.assertEqual(self.sube.saldo, 1000)
        self.assertEqual(self.sube.grupo_beneficiario, None)
        self.assertEqual(self.sube.estado, ACTIVADO)

    def test_obtener_precio_ticket(self):
        precio_ticket = self.sube.obtener_precio_ticket()

        self.assertEqual(precio_ticket, PRECIO)

    def test_obtener_precio_ticket_con_grupo_beneficiario(self):
        sube = Sube()
        sube.saldo = 1000
        sube.grupo_beneficiario = PRIMARIO
        precio_ticket = sube.obtener_precio_ticket()

        self.assertEqual(precio_ticket, 35)

    def test_pagar_pasaje_con_saldo(self):
        self.sube.pagar_pasaje()
        self.assertEqual(
            self.sube.saldo,
            950,
        )

    def test_imposible_pagar_pasaje_sin_saldo(self):
        sube = Sube()
        sube.saldo = 30
        with self.assertRaises(NoHaySaldoException):
            sube.pagar_pasaje()

    def test_imposible_pagar_pasaje_con_usuario_desactivado(self):
        sube = Sube()
        sube.saldo = 500
        sube.estado = DESACTIVADO

        with self.assertRaises(UsuarioDesactivadoException):
            sube.pagar_pasaje()

    def test_pagar_pasaje_con_grupo_beneficiario(self):
        sube = Sube()
        sube.saldo = 35
        sube.grupo_beneficiario = PRIMARIO

        sube.pagar_pasaje()
        self.assertEqual(
            sube.saldo,
            0,
        )

    def test_cambiar_estado_sube_a_desactivado(self):
        estado = DESACTIVADO
        self.sube.cambiar_estado(estado)
        self.assertEqual(
            self.sube.estado,
            DESACTIVADO,
        )

    def test_cambiar_estado_sube_a_activado(self):
        sube = Sube()
        sube.estado = DESACTIVADO

        sube.cambiar_estado(ACTIVADO)

        self.assertEqual(
            sube.estado,
            ACTIVADO,
        )

    def test_imposible_cambiar_a_estado_no_existente(self):
        estado = 'pendiente'
        with self.assertRaises(EstadoNoExistenteException):
            self.sube.cambiar_estado(estado)

    def test_pagar_pasaje_con_grupo_beneficiario_secundario(self):
        sube = Sube()
        sube.saldo = 42
        sube.grupo_beneficiario = SECUNDARIO

        with self.assertRaises(NoHaySaldoException):
            sube.pagar_pasaje()

        self.assertEqual(
            sube.saldo,
            42,
        )


if __name__ == '__main__':
    unittest.main()