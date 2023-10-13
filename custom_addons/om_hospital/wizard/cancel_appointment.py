from odoo import api, fields, models


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "cancel appointment"

    appointment_id = fields.Many2one("hospital.appointment", string="Appointment")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        return
