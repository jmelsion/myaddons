# -*- coding: utf-8 -*-

from odoo import models, fields, api


class app_prova(models.Model):
    _name = 'app_prova.app_prova'
    _description = 'app_prova.app_prova'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad > 10:
                record.urgente = True
            else:
                record.urgente = False
