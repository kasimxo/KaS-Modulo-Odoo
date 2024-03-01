# -*- coding: utf-8 -*-

from odoo import models
from odoo import fields
from odoo import api

class libreria(models.Model):
    _name = 'libreria.libreria'
    _description = 'libreria.libreria'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
            
class webinar_damabl(models.Model):
    _name="libreria.clase"
    _description = 'libreria.clase'
    name = fields.Char(string="Nombre", required = True, help="Nombre de la clase")
    descripcion = fields.Text(string="Descripción")
    horas = fields.Integer(string="Horas a la semana")
    lugar = fields.Char(string="Lugar")
    profesores_id = fields.One2many("libreria.profesores","clase_id",string="Profesores")


class webinar_profesores(models.Model):
    _name="libreria.profesores"
    _description = 'libreria.profesores'
    name = fields.Char(string="Nombre", required = True, help="Nombre del profesor")
    telefono = fields.Text(string="Teléfono")
    fecha_nac = fields.Date(string="Fecha de nacimiento")
    lugar = fields.Char(string="Lugar")
    clase_id = fields.Many2one("libreria.clase",string="Clase",required=True,ondelete="cascade")


