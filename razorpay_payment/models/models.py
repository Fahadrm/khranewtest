# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RazorpayPaymentRule(models.Model):
    _name = 'razorpay.payment.rule'
    _description = 'Razorpay Payment Rule'

    name = fields.Char(required=True, translate=True, copy=False,)
    code = fields.Char(required=True, help="The code of payment rules can be used as reference. "
                                           "In that case, it is case sensitive.", copy=False,)
    amount_percentage = fields.Float(string='Percentage (%)', digits='Razorpay Rate',
                                     help='For example, enter 50.0 to apply a percentage of 50%')

    _sql_constraints = [
        ('code_uniq', 'unique(code)', "A code can only be assigned to one rule !"),
    ]


