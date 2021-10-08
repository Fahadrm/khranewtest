# -*- coding: utf-8 -*-
# from odoo import http


# class RazorpayPayment(http.Controller):
#     @http.route('/razorpay_payment/razorpay_payment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/razorpay_payment/razorpay_payment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('razorpay_payment.listing', {
#             'root': '/razorpay_payment/razorpay_payment',
#             'objects': http.request.env['razorpay_payment.razorpay_payment'].search([]),
#         })

#     @http.route('/razorpay_payment/razorpay_payment/objects/<model("razorpay_payment.razorpay_payment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('razorpay_payment.object', {
#             'object': obj
#         })
