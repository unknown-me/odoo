from odoo import models, fields


class specialization(models.Model):
    _name = "hospital_mgmt.specialization"

    type = fields.Char(strng="specialization Type")
    spec_id = fields.One2many("hospital_mgmt.doctor", 'specialization_id', ondelete="restrict", index=True, readonly=True)
