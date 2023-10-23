from odoo import api, fields, models
from datetime import date

from odoo.exceptions import ValidationError


class DoctorDetails(models.Model):
    _name = "doctor.details"
    _description = "doctor details"
    name = fields.Char(string='Name')
    mobile = fields.Char('Mobile', compute='_compute_mobile', readonly=False, store=True)
    date_of_birth = fields.Date(string="Date of birth")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    bio = fields.Text(string="Bio")
    degree = fields.Text(string="Degree")
    specialization = fields.Text(string="specialization")

    @api.constrains('mobile')
    def _compute_mobile(self):

        for rec in self:

            if rec.mobile and len(rec.mobile) != 10:
                raise ValidationError("invalid mobile number")

        return True
