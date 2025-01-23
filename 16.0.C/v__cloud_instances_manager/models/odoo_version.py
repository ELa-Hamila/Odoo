from odoo import fields, models


class OdooVersion(models.Model):
    _name = "odoo.version"
    _description = "Odoo version details"
    _order = "name"
    name = fields.Char(string="Name", required=False)
