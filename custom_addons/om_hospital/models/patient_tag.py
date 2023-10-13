from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _description = "patient tag"
    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string="active", default=True)
    color = fields.Integer(string="Color")
    color_2 = fields.Char(string="Color 2")