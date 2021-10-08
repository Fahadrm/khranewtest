# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ConfigureWebhook(models.Model):
    _inherit = 'configure.webhook'

    razorpay_auth_key = fields.Char(string="Auth Key", required=True)
    razorpay_settlement_recon_url = fields.Char(string="URL", required=True, default="https://api.razorpay.com/v1/settlements/recon/combined")
    razorpay_api_key = fields.Char(string="Api Key", required=True)



