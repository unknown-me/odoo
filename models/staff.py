from odoo import models, api, fields


class StaffType(models.Model):
    _name = "hospital_mgmt.staff_type"
    _rec_name = "type_name"

    type_name = fields.Char(string="Staff Type Name", required=True)
    _sql_constraints = [("type_name", "unique(type_name)", "Staff Type must be unique!")]


class StaffIdSequenceGeneration(models.Model):
    _inherit = "hospital_mgmt.staff"

    @api.model
    def create(self, vals_list):
        if self.env['hospital_mgmt.staff_type'].search([('id', '=', vals_list["staff_type"])]).type_name == "Doctor":
            print("in if:")
            vals_list["staff_id"] = self.env['ir.sequence'].next_by_code('sequence.doctor_id')
        else:
            vals_list["staff_id"] = self.env['ir.sequence'].next_by_code('sequence.other_staff_id')
        return super(StaffIdSequenceGeneration, self).create(vals_list)