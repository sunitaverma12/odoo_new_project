from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "hospital patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date of birth")
    ref = fields.Char(string="Reference")
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many("patient.tag", string="Tags")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 1

    @api.model
    def create(self,vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).create(vals)

    def write(self, vals):
        if not self.ref and not vals.get('ref'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(HospitalPatient, self).write(vals)

    def name_get(self):
        return [(record.id, "[%s] %s" % (record.ref, record.name)) for record in self]