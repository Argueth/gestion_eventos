# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Budget_Abstract(models.AbstractModel):
    _name = 'gestion_eventos.budget_abstract'
    _description = 'Budget'

    code = fields.Integer(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)
    
    line_ids = fields.One2many('gestion_eventos.line', 'code', string='Líneas')
    
    total_price = fields.Float(string='Precio', compute='compute_total_price', store=True)

    events_ids = fields.Many2many('gestion_eventos.event', string='Eventos')
    
    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(name)','Name must be unique.')
    ]

    @api.depends('line_ids.price')
    def compute_total_price(self):
        for r in self:
            r.total_price = sum(r.line_ids.mapped('price'))