class VentaDetalle:
    """ Clase que implementa detalle de una venta"""
    def __init__(self, item, codigo, nombre, marca, cantidad,precio_unitario) -> None:
        self.item=item
        self.codigo=codigo
        self.nombre=nombre
        self.marca = marca
        self.cantidad=cantidad
        self.precio_unitario=precio_unitario
        self.base_imponible=(cantidad*precio_unitario)/1.18
        self.igv=(cantidad* precio_unitario)-(cantidad*precio_unitario)/1.18
        self.total=cantidad*precio_unitario
        
        pass
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|{}|{}|{}|".format(self.item,
                                    self.codigo,
                                    self.nombre,
                                    self.marca,
                                    self.cantidad,
                                    round(self.precio_unitario,2),
                                    round(self.base_imponible,2),
                                    round(self.igv,2),
                                    round(self.total,2))