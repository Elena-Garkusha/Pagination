# -*- coding: utf-8 -*-
from openerp import http

class Pagination(http.Controller):
    @http.route('/pagination/', auth='public', website=True)
    def index(self, **kw):
         Products = http.request.env['pagination.pagination']
         return http.request.render('pagination.index', {
             'products': Products.search([])
         })
    @http.route('/pagination/page2/', auth='public', website=True)
    def page2(self, **kw):
         Products = http.request.env['pagination.pagination']
         return http.request.render('pagination.page2', {
             'products': Products.search([])
         })