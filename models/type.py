# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Type(models.Model):
    _name = 'gestion_eventos.type'
    _description = 'Type'

    code = fields.Integer(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)
    
    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(name)','Name must be unique.')
    ]