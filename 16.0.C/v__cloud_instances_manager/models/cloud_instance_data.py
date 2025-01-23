from odoo.addons.base.models import ir_actions
from odoo import api


class CloudInstanceAutomation(ir_actions):
    @api.model
    def run(self, record):
        self.show_password = False
