# -*- coding: utf-8 -*-
# from odoo import http


# class CrmRequestManagement(http.Controller):
#     @http.route('/crm_request_management/crm_request_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_request_management/crm_request_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_request_management.listing', {
#             'root': '/crm_request_management/crm_request_management',
#             'objects': http.request.env['crm_request_management.crm_request_management'].search([]),
#         })

#     @http.route('/crm_request_management/crm_request_management/objects/<model("crm_request_management.crm_request_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_request_management.object', {
#             'object': obj
#         })
