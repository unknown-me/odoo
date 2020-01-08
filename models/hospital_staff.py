from odoo import models, fields

class doctors(models.Model):
    _name = "hospital_mgmt.doctor"

    type = fields.Many2one("hospital_mgmt.type", string="hospital.mgmt.doctor_type.type")
    staff_id = fields.Many2one("hospital_mgmt.staff", string="hospital_mgmt.staff.type", ondelete="restrict", required=True)
    specialization_id = fields.Many2one("hospital_mgmt.specialization", ondelete="restrict")