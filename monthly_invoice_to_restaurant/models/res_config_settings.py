# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    send_invoice_to_restaurant = fields.Boolean('Send Invoice to Restaurant', config_parameter='monthly_invoice_to_restaurant.send_invoice_to_restaurant')

