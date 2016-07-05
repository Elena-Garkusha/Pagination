# -*- coding: utf-8 -*-

from openerp import models, fields, api

class pagination(models.Model):
    _name = 'pagination.pagination'

    name = fields.Char()