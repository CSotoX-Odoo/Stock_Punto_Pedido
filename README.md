# CRE 20/FEB/2018 (CSOTOX)

Mejora a la Aplicación de Inventario (Stock) del ERP ODOO

Agrega un Informe al Inventario, que permite visualizar en cualquier 
momento los productos que poseen un Stock Bajo, o sea, estan en Punto de 
pedido.

Este informe lee la configuración de cada producto almacenable desde las reglas 
de abastecimiento para saber el Stock Minimo y Maximo que se deberia tener en 
inventario a mano.

Por lo tanto, para los productos a que se desee hacer un seguimiento de su nivel
de Stock, basta con crear una regla de abastecimiento y establecer el nivel de 
Stock Minimo y Maximo.

Para la documentación, solicitudes de mejoras o nuevas funcionalidades, así
como reportar algun Bug, por favor, visita la pagina: 
https://github.com/OdooX/Stock_Punto_Pedido

Se puede generar un Informe PDF con todos los productos listados o solamente
los productos que fueron seleccionados.

