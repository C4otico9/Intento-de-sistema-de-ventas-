class Persona:
    """Clase que implementa persona"""
    def __init__(self,id="", dni="", nombres="",apellidos="", direccion="",telefono="") -> None:
        self.id=id
        self.dni=dni
        self.nombres=nombres
        self.apellidos=apellidos
        self.direccion=direccion
        self.telefono=telefono
    
    def convertir_a_string(self):
        return "|{}|{}|{}|{}|{}|{}|".format(self.id,
                                            self.dni,
                                            self.nombres,
                                            self.apellidos,
                                            self.direccion,
                                            self.telefono)
        