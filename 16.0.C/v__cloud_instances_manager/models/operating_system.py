from odoo import fields, models


class OperatingSystem(models.Model):
    _name = "operating.system"
    _description = "Operating System"
    _order = "name"
    name = fields.Char(string="Name", required=False)
