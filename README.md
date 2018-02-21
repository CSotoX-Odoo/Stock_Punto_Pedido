# Brach para la versión 11 de Odoo
# URL: https://github.com/OdooX/Stock_Punto_Pedido

Este plus-in agrega una nueva funcionalidad a la aplicación de Inventario (Stock) del ERP ODOO.

La instalación base de Odoo posee una tarea programada que se ejecuta una vez al día, esta lee las Reglas de Abastecimiento y compara los Stock, en caso de encontrar Stock a Mano por debajo del Stock Mínimo registra una Actividad (Alerta) para el usuario, notificando los productos que poseen Stock Bajo.

Por lo tanto, el usuario encargado de realizar las Solicitudes de Abastecimiento, no puede hacer un seguimiento en tiempo real o al momento oportuno de los productos que poseen Stock Bajo.

Por esta razón, este plus-in agrega una vista al menú Informe de la Aplicación de Inventario, que permite visualizar en el momento deseado los productos que poseen un Stock Bajo, o sea, productos donde el Stock a Mano es menor o igual que el Stock Mínimo requerido.

El Stock Mínimo requerido se configura a través de las Reglas de Abastecimiento, por lo tanto, si el producto tiene Regla de Abastecimiento, y su Stock a Mano es menor a la regla de Stock Mínimo, sera mostrado en dicho listado.

Si no desea hacer un seguimiento a un determinado producto, basta con eliminar la Regla de Abastecimiento asociada al mismo.

También se agrega la opción al menú de Imprimir, donde se generar un Informe PDF con todos los productos listados o solamente los productos que fueron seleccionados.

Nota: Si esta funcionalidad es de interés para usted, por favor, no dude en participar de este proyecto, ya sea mejorando el código, sugiriendo nuevas funcionalidades o mejoras.

Me despido con un cordial saludo.
