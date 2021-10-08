# -*- coding: utf-8 -*-

from odoo import models, fields, api
import razorpay
import requests
from requests.auth import HTTPBasicAuth
import json


class RazorpaySettlementCompute(models.TransientModel):
    _name = 'razorpay.settlement.compute'
    _description = 'Run Razorpay Settlement Manually'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    settlement_id = fields.Integer(string='Settlement ID')

    def action_razorpay_fetch(self):
        webhook = self.env["configure.webhook"].search([], limit=1)
        api_key = webhook.razorpay_api_key
        secret = webhook.razorpay_auth_key
        day = self.date.day

        query = {'year': self.date.year, 'month': self.date.month}
        method = "get"
        url = webhook.razorpay_settlement_recon_url
        auth = HTTPBasicAuth(api_key, secret)
        rsp = requests.request(method, url, headers=None, auth=auth, params=query)
        settlements = rsp.json()
        print(rsp.json())

