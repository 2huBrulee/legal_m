# -*- coding: utf-8 -*-
from odoo import http

# class LegalM(http.Controller):
#     @http.route('/legal_m/legal_m/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/legal_m/legal_m/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('legal_m.listing', {
#             'root': '/legal_m/legal_m',
#             'objects': http.request.env['legal_m.legal_m'].search([]),
#         })

#     @http.route('/legal_m/legal_m/objects/<model("legal_m.legal_m"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('legal_m.object', {
#             'object': obj
#         })