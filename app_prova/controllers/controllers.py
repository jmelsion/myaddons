# -*- coding: utf-8 -*-
# from odoo import http


# class AppProva(http.Controller):
#     @http.route('/app_prova/app_prova', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/app_prova/app_prova/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('app_prova.listing', {
#             'root': '/app_prova/app_prova',
#             'objects': http.request.env['app_prova.app_prova'].search([]),
#         })

#     @http.route('/app_prova/app_prova/objects/<model("app_prova.app_prova"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('app_prova.object', {
#             'object': obj
#         })
