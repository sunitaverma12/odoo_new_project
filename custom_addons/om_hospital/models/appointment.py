from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "patient appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "ref"
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")
    ref = fields.Char(string="Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very high')], string='Priority')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')], string='Status', requied=True, default="draft")
    doctor_id = fields.Many2one('res.users', string="Doctor")
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.line', 'appointment_id', string="Pharmacy Line")

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref = self.patient_id.ref

    def action_test(self):
        print("click!!!")
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Click successfully',
                'type': 'rainbow_man',

            }
        }

    def action_in_consultation(self):
        for rec in self:
            rec.state = "in_consultation"

    def action_done(self):
        for rec in self:
            rec.state = "done"

    def action_cancel(self):
        action = self.env.ref('om_hospital.cancel_appointment_act').read()[0]
        return action

    def action_draft(self):
        for rec in self:
            rec.state = "draft"


class AppointmentPharmacyLine(models.Model):
    _name = "appointment.pharmacy.line"
    _description = " appointment pharmacy line"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(string='Price')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
