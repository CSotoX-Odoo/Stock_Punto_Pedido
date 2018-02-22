# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 21/FEB/2018 (CSOTOX)

from odoo import api, fields, models, _

class Punto_Pedido(models.Model):
    _inherit = "product.template"
    x_punto_pedido = fields.boolean(compute='_CalcularPunto', string='Esta en punto de pedido')    

    @api.one
    def _CalcularPunto(self):
        self.x_punto_pedido = True
