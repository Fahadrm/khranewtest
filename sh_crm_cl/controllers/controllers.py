# -*- coding: utf-8 -*-
# from odoo import http


# class ShCrmCl(http.Controller):
#     @http.route('/sh_crm_cl/sh_crm_cl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sh_crm_cl/sh_crm_cl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sh_crm_cl.listing', {
#             'root': '/sh_crm_cl/sh_crm_cl',
#             'objects': http.request.env['sh_crm_cl.sh_crm_cl'].search([]),
#         })

#     @http.route('/sh_crm_cl/sh_crm_cl/objects/<model("sh_crm_cl.sh_crm_cl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sh_crm_cl.object', {
#             'object': obj
#         })
