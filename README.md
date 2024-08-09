# FarmCamp

## Descripción 
Sistema integral de gestión que permite manejar todas las operaciones relacionadas con la administración de medicamentos, proveedores, empleados, pacientes, así como la generación de informes relevantes.

Dentro de este programa el acceso a los modulos está organizado por medio de menús en los cuales, dependiendo de la opción que escoja el usuario se le dará el acceso a los diferentes apartados.

## Tecnologías usadas
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)

## Características
|Archivo|Función|
|--|--|
|**Farmacia.py**|Archivo en que está el código del programa en sí|
|**Compras.json**|Archivo en el que se van a almacenar los datos del historial de compras|
|**Empleados.json**|Archivo en el que están almacenados los datos de los empleados de la farmacia|
|**Medicamentos.json**|Archivo en el que están almacenados todos los datos de los medicamentos, inclyendo su nombre, precio, stock, etc.|
|**Pacientes.json**|Archivo en el que están almacendos los datos de los pacientes, como lo son el nombre, su dirección y teléfono de contacto|
|**Proveedores.json**|Archivo en el que están almacenados los datos de los proveedores a los que se les compran los medicamentos|
|**Ventas.json**|Archivo en el que se van a almacenar los datos del historial de ventas de la farmacia|

## Funcionalidades

El programa está dividido en diferentes modulos, los cuales contienen diferentes funcionalidades, que son:
### Gestión de Ventas y Compras:
***Ventas:*** El sistema debe permitir registrar cada transacción de venta con la siguiente información:
  - Fecha de la venta.
  - Información del paciente (nombre, dirección).
  - Información del empleado que realizó la venta (nombre, cargo).
  - Medicamentos vendidos (nombre, cantidad, precio).

***Compras:*** El sistema debe permitir registrar cada compra realizada a los proveedores con la siguiente información:
  - Fecha de la compra.
  - Información del proveedor (nombre, contacto).
  - Medicamentos comprados (nombre, cantidad, precio de compra).

## Instrucciones de uso

1. Debes clonar este repositorio en tu maquina local, copia el siguiente código y lo pegas en bash
```bash
git clone https://github.com/BrayanStivenMaldonado/Trabajo_Python_Farmacia_MaldonadoBrayan.git
```

2. Dentro de VSC vas a ejecutar el archivo .py en la terminal o con alguna extension, por ejemplo **CodeRunner**

## Desarrollado

Este programa fue desarrollado por ***Brayan Maldonado***, estudiante de Campuslands.
