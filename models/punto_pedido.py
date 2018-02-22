# -*- coding: utf-8 -*-

# Carlos Rafael Soto (CSotoX)
# Odoo.soporte@gmail.com
# Odoo v11

# CRE 21/FEB/2018 (CSOTOX)
#      Se agrega el campo x_punto_pedido en el modelo product.template este campo calculado
#      tiene la finalidad de True en caso de que el producto este en Punto de Pedido

from odoo import api, fields, models, _

class Punto_Pedido(models.Model):
    _inherit = "product.template"
    x_punto_pedido = fields.Boolean(compute='_CalcularPunto', string='Esta en punto de pedido', store=True)    

    @api.one
    def _CalcularPunto(self):
        # Siempre inicio el valor del campo en false
        self.x_punto_pedido = False

        # Verifico si tiene regla de abastecimiento
        if self.nbr_reordering_rules > 0:
            # Si tiene regla de abastecimiento, verifico que el Stock a Mano sea menor
            # o igual a la regla de Stock Mínimo
            if self.qty_available <= self.reordering_min_qty:
                self.x_punto_pedido = True

            