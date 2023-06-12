PRECIO = 50
PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
ACTIVADO = 'activado'
DESACTIVADO = 'desactivado'

class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class Sube:
    def __init__(self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario == PRIMARIO:
            return 35
        else:
            return PRECIO

    def pagar_pasaje(self):
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException

        if self.saldo < self.obtener_precio_ticket():
            raise NoHaySaldoException

        precio_ticket = self.obtener_precio_ticket()
        self.saldo = self.saldo - precio_ticket

    def cambiar_estado(self, estado):
        if estado not in (ACTIVADO, DESACTIVADO):
            raise EstadoNoExistenteException
        self.estado = estado