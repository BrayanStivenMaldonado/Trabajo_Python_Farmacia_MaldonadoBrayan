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

    elif Eleccion == 3: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        system("cls")
        boolGeneral = False
    
    else: 
        input("Esta no es una opción válida, presione ENTER para continuar")
        system("cls")