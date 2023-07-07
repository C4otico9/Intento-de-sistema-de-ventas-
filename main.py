import datetime
from persona import Persona
from producto import Producto
from venta_detalle import VentaDetalle
from venta import Venta
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generar_factura_pdf(venta: Venta):
    # Crea el archivo PDF
    pdf = canvas.Canvas('factura.pdf', pagesize=letter)

    # Configura el estilo de fuente
    pdf.setFont("Helvetica", 12)

    # Fecha actual
    fecha_actual = datetime.date.today()
    fecha_actual_str = fecha_actual.strftime("%d/%m/%Y")
   

    # Agrega el encabezado de la factura
    pdf.drawString(50, 750, "FACTURA")
    pdf.drawString(50, 700, "Nro: {}".format(venta.numero))
    pdf.drawString(50, 650, "Fecha: {}".format(fecha_actual_str))
    pdf.drawString(50, 600, "Cliente: {} {}".format(venta.cliente.nombres.title(), venta.cliente.apellidos.title()))
    pdf.drawString(50, 550, "Dirección: {}".format(venta.cliente.direccion.title()))
    pdf.drawString(50, 500, "Teléfono: {}".format(venta.cliente.telefono))
    
    # Agrega el detalle de la venta
    y = 450
    for detalle in venta.detalle:
        pdf.drawString(50, y, "Producto: {}".format(detalle.nombre.title()))
        pdf.drawString(200, y, "Marca: {}".format(detalle.marca.title()))
        pdf.drawString(350, y, "Cantidad: {}".format(detalle.cantidad))
        pdf.drawString(500, y, "Precio unitario: {}".format(detalle.precio_unitario))
        pdf.drawString(650, y, "Subtotal: {}".format(detalle.total))
        y -= 20

    # Agrega el total de la venta
    pdf.drawString(50, y, "Total: {}".format(venta.total))

    # Guarda el archivo PDF
    pdf.save()

    print("Factura generada en factura.pdf")
""" crear un CRUD de persona"""
datos_inicial:list=[{"dni":"73306251",
                     "nombres":"Walter Geronimo",
                     "apellidos":"Cayte Sejje",
                     "direccion":"Sda. Huancane" ,
                     "telefono":"920407364"},

                     {"dni":"733062511",
                     "nombres":"Walter Geronimo1",
                     "apellidos":"Cayte Sejje1",
                     "direccion":"Sda. Huancane1" ,
                     "telefono":"9204073641"},

                     {"dni":"733062512",
                     "nombres":"Walter Geronimo2",
                     "apellidos":"Cayte Sejje2",
                     "direccion":"Sda. Huancane2" ,
                     "telefono":"9204073642"}
                     ]
lista_personas:Persona=[]


def cargar_personas():
    for dato in datos_inicial:
        lista_personas.append(Persona(len(lista_personas),
                                dato["dni"],
                                dato["nombres"],
                                dato["apellidos"],
                                dato["direccion"],
                                dato["telefono"]))
    return lista_personas

def insertar_persona():
    dni:str = input("Ingrese DNI: ")
    nombres:str = input("Ingrese nombre: ")
    apellidos:str = input("Ingrese apellidos: ")
    direccion:str = input("Ingrese dirección: ")
    telefono:str = input("Ingrese teléfono: ")
    lista_personas.append(Persona(len(lista_personas)+1,dni,nombres.title(),apellidos.title(),direccion.title(),telefono))
    return lista_personas

def listar_personas():
    print("======================LISTA DE PERSONAS=============================")
    print("====================================================================")
    print("|ID|  DNI   |   NOMBRES  |  APELLIDOS  |  DIRECCION | TELEFONO|")
    print("====================================================================")
    for person in lista_personas:
        print("_______________________________________________________________")
        print(person.convertir_a_string())
        print("_______________________________________________________________")

def bucar_persona():
    dni:str = input("Ingrese DNI de la persona: ")
    for persona in lista_personas:
        if persona.dni == dni:
            print(persona.convertir_a_string())
            return persona

def editar_persona():
    listar_personas()
    dni:str = input("Ingrese DNI de la persona: ")
    for persona in lista_personas:
        if persona.dni == dni:
            print(persona.convertir_a_string())
            persona.dni = input("Ingrese DNI: ")
            persona.nombres = input("Ingrese nombre: ")
            persona.apellidos = input("Ingrese apellidos : ")
            persona.direccion = input("Ingrese dirección: ")
            persona.telefono = input("Ingrese el teléfono: ")
    listar_personas()

def eliminar_persona():
    listar_personas()
    dni:str = input("Ingrese DNI:  ")
    for index, persona in enumerate(lista_personas):
        if persona.dni == dni:
            lista_personas.pop(index)
    listar_personas()

""" crear un CRUD de producto"""
datos_inicial_productos:list=[{"codigo":"ROT001",
                     "nombre":"Rotomartillo",
                     "marca": "Uyustools",
                     "precio":170.00},
                    {"codigo":"HID002",
                     "nombre":"Hidrolavadora",
                     "marca":"Uyustools",
                     "precio":250.00},
                    {"codigo":"ESM003",
                     "nombre":"Esmeril",
                     "marca":"Truper",
                     "precio":100.00},
                     ]
lista_productos:Producto=[]


def cargar_productos():
    for dato in datos_inicial_productos:
        lista_productos.append(Producto(
                                dato["codigo"],
                                dato["nombre"],
                                dato["marca"],
                                dato["precio"]))
    return lista_productos

def insertar_producto():
    codigo:str = input("Ingrese codigo: ")
    nombre:str = input("Ingrese nombre: ")
    marca:str = input("Ingrese marca: ")
    precio:float = float(input("Ingrese precio: "))
    lista_productos.append(Producto(codigo,nombre.title(),marca.title(), precio))
    return lista_productos

def listar_productos():
    print("======================LISTA DE PRODUCTOS=========================")
    print("================================================================")
    print("|CODIGO|  NOMBRE   |   PRECIO  |")
    print("================================================================")
    for producto in lista_productos:
        print("_______________________________________________________________")
        print(producto.convertir_a_string())
        print("_______________________________________________________________")

def bucar_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    for producto in lista_productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_string())
            return producto

def editar_producto():
    listar_productos()
    codigo:str = input("Ingrese codigo del producto: ")
    for producto in lista_productos:
        if producto.codigo == codigo:
            print(producto.convertir_a_string())
            producto.nombre = input("Ingrese nombre del producto: ")
            producto.precio = input("Ingrese precio del producto: ")
            
    listar_productos()

def eliminar_producto():
    listar_productos()
    codigo:str = input("Ingrese codigo del producto: ")
    for index, producto in enumerate(lista_productos):
        if producto.codigo == codigo:
            lista_productos.pop(index)
    listar_productos()
    return lista_productos
venta_detalles:VentaDetalle=[]

def agregar_productos():
    producto:Producto=bucar_producto()
    cantidad:float=float(input("Ingrese la cantidad: "))
    venta_detalles.append(VentaDetalle(len(venta_detalles)+1,producto.codigo,producto.nombre, producto.marca,cantidad,producto.precio))
    return venta_detalles
ventas:Venta=[]
def insertar_venta():
    cliente = bucar_persona()
    continuar_agregando_producto = True
    while continuar_agregando_producto:
        opcion = input("1 para agregar producto, 2 para guardar venta: ")
        if opcion == "1":
            agregar_productos()
        elif opcion == "2":
            continuar_agregando_producto = False

    total_venta = 0
    for venta_detalle in venta_detalles:
        print(venta_detalle.convertir_a_string())
        total_venta += venta_detalle.total
    venta = Venta(len(ventas) + 1, cliente, venta_detalles, total_venta)
    ventas.append(venta)

    generar_factura_pdf(venta)
    return ventas

def listar_ventas():
    for venta in ventas:
        print(venta.convertir_a_string())
    return ventas
  
def buscar_venta():
    numero:int=int(input("Ingrese el numero de la venta: "))
    for venta in ventas:
        if venta.numero==numero:
            print(venta.convertir_a_string())
            for detalle in venta.detalle:
                print(detalle.convertir_a_string())
            return venta


def menu_texto():
    print("=============MENU============")
    print("=========CRUD PERSONA========")
    print("OPCION 1 PARA CREAR PERSONA")
    print("OPCION 2 PARA LISTAR")
    print("OPCION 3 PARA BUSCAR PERSONA")
    print("OPCION 4 PARA EDITAR PERSONA")
    print("OPCION 5 PARA ELIMINAR PERSONA")
    print("=========CRUD PRODUCTO========")
    print("OPCION 6 PARA CREAR PRODUCTO")
    print("OPCION 7 PARA LISTAR PRODUCTO")
    print("OPCION 8 PARA BUSCAR PRODUCTO")
    print("OPCION 9 PARA EDITAR PRODUCTO")
    print("OPCION 10 PARA ELIMINAR PRODUCTO")
    print("=========CRUD VENTA========")
    print("OPCION 11 PARA REGISTRAR VENTA")
    print("OPCION 12 PARA LISTAR VENTA")
    print("OPCION 13 PARA BUSCAR VENTA")
    print("OPCION 30 PARA SALIR")

def menu():
    continuar:bool=True
    while continuar:
        menu_texto()  
        opcion:str
        opcion = input("Ingrese la opción: ")
        match opcion:
            case "1":
                insertar_persona()
            case "2": 
                listar_personas()
            case "3":
                bucar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                insertar_producto()
            case "7": 
                listar_productos()
            case "8":
                bucar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "11":
                insertar_venta()
            case "12":
                listar_ventas()
            case "13":
                buscar_venta()
            case "30":
                print("Saliendo del programa")
                continuar = False

def main():
    cargar_personas()
    cargar_productos()
    
    menu()    
    print("Iniciando programa")
    return True

if __name__== '__main__':
    main()
    insertar_venta()