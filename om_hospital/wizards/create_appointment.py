# -*- coding: utf-8 -*-

from odoo import models, fields, api,  _


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': 'Created From The Wizard/Code'
        }
        self.patient_id.message_post(body="Test string ", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("Get Data Function")
        appointments = self.env['hospital.appointment'].search([])
        print("appointments", appointments)
        for rec in appointments:
            print("Appointment Name", rec.name)




