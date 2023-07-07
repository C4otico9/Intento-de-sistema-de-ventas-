from persona import Persona
class Venta:
    """ Clase que implementa venta"""
    def __init__(self, numero, cliente:Persona, detalle:list=[],total:float=0) -> None:
        self.serie = 'F003'
        self.numero=numero
        self.cliente:Persona=cliente
        self.detalle:list=detalle
        self.base_imponible=total/1.18
        self.igv=total-(total/1.18)
        self.total=total
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|{}|".format(self.serie,
                                    self.numero,
                                    self.cliente.nombres,
                                    round(self.base_imponible,2),
                                    round(self.igv,2),
                                    round(self.total,2))