# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 20/FEB/2018 (CSOTOX)

{
    'name': 'Stock_Punto_Pedido',
    'version': '11.2.0',
    'category': 'Stock',
    'sequence': 10,
    'author' : 'Carlos Rafael Soto (CSOTOX)',
    'summary': 'Listado de productos con Stock Bajo (Punto de pedido)',
    'description': """
                    Versión de Odoo: 11
                    """,
    'website': 'https://github.com/OdooX/Stock_Punto_Pedido',
    'depends': [
        'product',
        'stock',
        'purchase', 
        ],
    'data': [
        'views/noti_stock_bajo_view.xml',

        'report/stock_reports_templates.xml',
        'report/stock_reports.xml',
        ],
    'installable': True,
    'application': False,
    'auto_install': False,
}