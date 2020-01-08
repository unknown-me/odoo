from odoo import models, fields, api

class doctor_type(models.Model):
    _name = "hospital_mgmt.doctor_type"

    doctor_type = fields.Char(strng="Doctor Type", required=True)
