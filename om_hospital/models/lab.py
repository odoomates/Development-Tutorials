# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalLab(models.Model):
    _name = 'hospital.lab'
    _description = 'Hospital Laboratory'

    name = fields.Char(string="Name", required=True)
    user_id = fields.Many2one('res.users', string='Responsible')