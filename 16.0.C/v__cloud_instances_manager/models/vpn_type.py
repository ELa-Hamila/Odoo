from odoo import fields, models


class VpnType(models.Model):
    _name = "vpn.type"
    _description = "Vpn type"
    _order = "name"
    name = fields.Char(string="Name", required=False)