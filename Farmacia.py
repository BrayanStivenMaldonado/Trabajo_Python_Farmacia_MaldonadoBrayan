import json
from os import system
from datetime import date

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE VENTAS
def abrirVentas():
    Ventas=[]
    with open('Ventas.json','r',encoding='utf-8') as openfile:
        Ventas = json.load(openfile)  
    return Ventas
def guardarVentas(miVenta): 
    with open("Ventas.json","w",encoding='utf-8') as outfile:
        json.dump(miVenta,outfile,indent=4) 

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE PACIENTES
def abrirPacientes():
    Pacientes=[]
    with open('Pacientes.json','r',encoding='utf-8') as openfile:
        Pacientes = json.load(openfile)  
    return Pacientes
def guardarPacientes(miPaciente): 
    with open("Pacientes.json","w",encoding='utf-8') as outfile:
        json.dump(miPaciente,outfile,indent=4) 

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE EMPLEADOS
def abrirEmpleados():
    Empleados=[]
    with open('Empleados.json','r',encoding='utf-8') as openfile:
        Empleados = json.load(openfile)  
    return Empleados
def guardarEmpleados(miEmpleado): 
    with open("Empleados.json","w",encoding='utf-8') as outfile:
        json.dump(miEmpleado,outfile,indent=4) 

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE MEDICAMENTOS
def abrirMedicamentos():
    Medicamentos=[]
    with open('Medicamentos.json','r',encoding='utf-8') as openfile:
        Medicamentos = json.load(openfile)  
    return Medicamentos
def guardarMedicamentos(miMedicamento): 
    with open("Medicamentos.json","w",encoding='utf-8') as outfile:
        json.dump(miMedicamento,outfile,indent=4) 

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE PROVEEDORES
def abrirProveedores():
    Proveedores=[]
    with open('Proveedores.json','r',encoding='utf-8') as openfile:
        Proveedores = json.load(openfile)  
    return Proveedores
def guardarProveedores(miProveedor): 
    with open("Proveedores.json","w",encoding='utf-8') as outfile:
        json.dump(miProveedor,outfile,indent=4) 

#FUNCIONES PARA ABRIR Y GUARDAR DATOS DEL JSON DE COMPRAS
def abrirCompras():
    Compras=[]
    with open('Compras.json','r',encoding='utf-8') as openfile:
        Compras = json.load(openfile)  
    return Compras
def guardarCompras(miCompra): 
    with open("Compras.json","w",encoding='utf-8') as outfile:
        json.dump(miCompra,outfile,indent=4) 

#INICIO DEL PROGRAMA
boolGeneral = True
while boolGeneral == True:
    Eleccion = int(input("---Bienvenido a FarmCamp---\n1. Ventas\n2. Compras \n3. Salir\n\n A qué apartado deseas acceder?: "))
    system("cls")

    #VENTAS
    if Eleccion == 1: 
        print("---VENTAS---\n")
        Fecha = date.today()
        FechaVenta = Fecha.isoformat()
        system("cls")

        # PACIENTES
        Pacientes = abrirPacientes()
        contador = 1
        print("Pacientes\n\nid  Nombre  Dirección   Telefono")
        for i in Pacientes:
            print(contador,"|",i["nombre"],"|",i["direccion"],"|",i["telefono"])
            contador += 1
        ElePaciente = int(input("\nIngrese el id del paciente: "))
        NombrePaciente = Pacientes[ElePaciente-1]["nombre"]
        DireccionPaciente = Pacientes[ElePaciente-1]["direccion"]
        system("cls")

        #EMPLEADOS
        Empleados = abrirEmpleados()
        contador = 1
        print("Empleados\n\nid  Nombre   Cargo")
        for i in Empleados:
            print(contador,"|",i["nombre"],"|",i["cargo"])
            contador += 1
        EleEmpleado = int(input("\nIngrese el id del empleado: "))
        NombreEmpleado  = Empleados[EleEmpleado-1]["nombre"]
        CargoEmpleado = Empleados[EleEmpleado-1]["cargo"]
        system("cls")

        #MEDICAMENTOS
        Medicamentos = abrirMedicamentos()
        contador = 1
        print("Medicamentos\n\nid     Nombre      Precio")
        for i in Medicamentos:
            print(contador,"|",i["nombre"],"|",i["precio"])
            contador += 1
        EleMedicamento = int(input("\nIngrese el id del medicamento: "))
        NombreMedicamento = Medicamentos[EleMedicamento-1]["nombre"]
        CantidadMedicamento = int(input("Ingrese la cantidad de medicamentos: "))
        PrecioMedicamento = Medicamentos[EleMedicamento-1]["precio"]
        PrecioFinal = PrecioMedicamento*CantidadMedicamento
        Stock = Medicamentos[EleMedicamento-1]["stock"]
        Stock -= CantidadMedicamento
        Medicamentos[EleMedicamento-1]["stock"] = Stock
        guardarMedicamentos(Medicamentos)

        system("cls")

        #Datos que se van agregar al json de ventas
        RegistroVentas = abrirVentas()
        RegistroVentas["HistorialVentas"].append(
            {
                "Fecha" : FechaVenta,
                "InfoPaciente" : {
                    "NombrePaciente" : NombrePaciente,
                    "DireccionPaciente" : DireccionPaciente
                },
                "InfoEmpleado" : {
                    "NombreEmpleado" : NombreEmpleado,
                    "CargoEmpleado" : CargoEmpleado
                },
                "MedicamentosVendidos" : {
                    "NombreMedicamento" : NombreMedicamento,
                    "CantidadMedicamento" : CantidadMedicamento, 
                    "PrecioMedicamento" : PrecioMedicamento,
                    "PrecioTotal" : PrecioFinal
                }
            }
        )
        guardarVentas(RegistroVentas)
        input("Venta registrada con éxito, presione ENTER para continuar")
        system("cls")
        
    #COMPRAS
    elif Eleccion == 2:
        print("---COMPRAS---")
        Fecha = date.today()
        FechaCompra = Fecha.isoformat()
        system("cls")

        #PROVEEDORES
        Proveedores = abrirProveedores()
        contador = 1
        print("Proveedores\n\nid    Nombre            Contacto                Direccion")
        for i in Proveedores:
            print(contador,"|",i["nombre"],"|",i["contacto"],"|",i["direccion"])
            contador += 1
        EleProveedor = int(input("\nIngrese el id del proveedor: "))
        NombreProveedor = Proveedores[EleProveedor-1]["nombre"]
        ContactoProveedor = Proveedores[EleProveedor-1]["contacto"]
        system("cls")

        #MEDICAMENTOS
        Medicamentos = abrirMedicamentos()
        contador = 1
        print("Medicamentos\n\nid     Nombre")
        for i in Medicamentos:
            print(contador,"|",i["nombre"])
            contador += 1
        EleMedicamentoCompra = int(input("\nIngrese el id del medicamento a comprar: "))
        NombreMedicamentoCompra = Medicamentos[EleMedicamentoCompra-1]["nombre"]
        CantidadMedicamentoCompra = int(input("\nIngrese la cantidad de medicamentos que va a comprar: "))
        PrecioMedicamentoCompra = int(input("\nIngrese el precio de compra de los medicamentos: "))
        PrecioTotal = PrecioMedicamentoCompra*CantidadMedicamentoCompra
        Stock = Medicamentos[EleMedicamentoCompra-1]["stock"]
        Stock += CantidadMedicamentoCompra
        Medicamentos[EleMedicamentoCompra-1]["stock"] = Stock
        guardarMedicamentos(Medicamentos)

        #Datos que se van a guardar en el json de compras
        Compras = abrirCompras()
        Compras["HistorialCompras"].append(
            {
                "Fecha" : FechaCompra,
                "InfoProveedor" : {
                    "NombreProveedor" : NombreProveedor,
                    "ContactoProveedor" : ContactoProveedor
                },
                "MedicamentosComprados" : {
                    "CantidadMedicamentoComprado" : CantidadMedicamentoCompra,
                    "PrecioMedicamentoComprado" : PrecioMedicamentoCompra,
                    "PrecioTotalCompra" : PrecioTotal
                }
            }
        )
        guardarCompras(Compras)
        input("Compra registrada con éxito, presione ENTER para continuar")
        system("cls")
        
    elif Eleccion == 3: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        system("cls")
        boolGeneral = False
    
    else: 
        input("Esta no es una opción válida, presione ENTER para continuar")
        system("cls")