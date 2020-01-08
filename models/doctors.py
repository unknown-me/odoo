from odoo import models, fields, api


class DoctorsFunctions(models.Model):
    _inherit = "hospital_mgmt.staff"

    def get_staff_type(self):
        print("log1", self)
        for _ in self:
            print("log2", _)