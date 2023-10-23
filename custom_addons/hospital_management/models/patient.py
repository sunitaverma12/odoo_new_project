from odoo import api, fields, models
from datetime import date

from odoo.exceptions import ValidationError


class HospitalPatients(models.Model):
    _name = "hospital.patients"
    _description = "hospital patients"
    name = fields.Char(string='Name')
    mobile = fields.Char('Mobile', compute='_compute_mobile', readonly=False, store=True)
    date_of_birth = fields.Date(string="Date of birth")
    age = fields.Integer(string="Age", compute="_compute_age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    id_proof = fields.Image(string="Id Proof")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.constrains('mobile')
    def _compute_mobile(self):

        for rec in self:

            if rec.mobile and len(rec.mobile) != 10:
                raise ValidationError("invalid mobile number")

        return True

