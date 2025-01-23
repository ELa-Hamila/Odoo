from odoo import fields, models


class HostingProvider(models.Model):
    _name = "hosting.provider"
    _description = "Hosting Provider"
    _order = "name"
    name = fields.Char(string="Name", required=False)
