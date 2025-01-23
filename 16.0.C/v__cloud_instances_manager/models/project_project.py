from odoo import fields, models, _


class ProjectProject(models.Model):
    _inherit = "project.project"

    instance_count = fields.Integer(
        string="Instance Count", compute="_cloud_instance_count"
    )

    def action_open_project(self):
        pass

    def action_open_cloud_instance(self):
        self.ensure_one()
        return {
            "name": _("Related instances"),
            "type": "ir.actions.act_window",
            "view_mode": "tree,form",
            "res_model": "cloud.instance",
            "domain": [("project_id", "=", self.id)],
        }

    def _cloud_instance_count(self):
        search = self.env["cloud.instance"].search([("project_id", "=", self.id)])
        self.instance_count = len(search)
