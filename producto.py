class Producto:
    """ Clase que implementa producto"""
    def __init__(self,codigo, nombre, marca, precio) -> None:
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.marca=marca
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|".format(self.codigo,
                                    self.nombre,
                                    self.marca,
                                    self.precio)
        