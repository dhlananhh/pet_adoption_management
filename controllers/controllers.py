# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddons\petAdoptionManagement\(http.Controller):
#     @http.route('/custom_addons\pet_adoption_management\/custom_addons\pet_adoption_management\', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addons\pet_adoption_management\/custom_addons\pet_adoption_management\/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addons\pet_adoption_management\.listing', {
#             'root': '/custom_addons\pet_adoption_management\/custom_addons\pet_adoption_management\',
#             'objects': http.request.env['custom_addons\pet_adoption_management\.custom_addons\pet_adoption_management\'].search([]),
#         })

#     @http.route('/custom_addons\pet_adoption_management\/custom_addons\pet_adoption_management\/objects/<model("custom_addons\pet_adoption_management\.custom_addons\pet_adoption_management\"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addons\pet_adoption_management\.object', {
#             'object': obj
#         })

