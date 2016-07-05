# -*- coding: utf-8 -*-
from openerp import http

class Pagination(http.Controller):
    @http.route('/pagination/', auth='public', website=True)
    def index(self, **kw):
         Products = http.request.env['pagination.pagination']
         return http.request.render('pagination.index', {
             'products': Products.search([])
         })