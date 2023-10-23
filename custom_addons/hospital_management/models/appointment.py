from odoo import api, fields, models


class HospitalAppointments(models.Model):
    _name = "hospital.appointments"
    _description = "patient appointments"
    _rec_name = "patient_id"

    patient_id = fields.Many2one('hospital.patients', string="Patient")
    gender = fields.Selection(related="patient_id.gender")
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")
    doctor_id = fields.Many2one("doctor.details", string="Physician")
    medicines_ids = fields.One2many("medicine.details", "appointment_id", string="medicine")
    vitals_ids = fields.One2many("vitals.details", "vitals", string="Vitals")
    symptoms_ids = fields.One2many("symptoms.details", "symptoms", string="Symptoms")


class MedicineDetails(models.Model):
    _name = "medicine.details"
    _description = " medicine details"

    medicine_id = fields.Many2one('medicine.patients', string="name")
    type = fields.Char(string='Type')
    qty = fields.Integer(string="Quantity")
    frequency = fields.Char(string="Frequency")
    appointment_id = fields.Many2one("hospital.appointments", string="Appointment")

    @api.onchange('medicine_id')
    def onchange_medicine_id(self):
        self.type = self.medicine_id.type


class VitalsDetails(models.Model):
    _name = "vitals.details"
    _description = " vitals details"

    temp = fields.Char(string='Temperature')
    bp = fields.Char(string="BP")
    weight = fields.Char(string="Weight")
    vitals = fields.Many2one("hospital.appointments", string="vital")


class SymptomsDetails(models.Model):
    _name = "symptoms.details"
    _description = " symptoms details"

    high_fever = fields.Char(string='High Fever')
    cold = fields.Char(string="Cold")
    flue = fields.Char(string="flue")
    symptoms = fields.Many2one("hospital.appointments", string="symptoms")
