from odoo import api, fields, models
from datetime import date


class MedicinePatients(models.Model):
    _name = "medicine.patients"
    _description = "medicine patients"
    name = fields.Char(string='Name')
    type = fields.Char(string="Type")
    expiry_date = fields.Date(string="Expiry Date")
