from odoo import fields, models, api
from odoo.addons.base.models.res_users import check_identity
import subprocess


class CloudInstance(models.Model):
    _name = "cloud.instance"
    _description = "cloud instance"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "title"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True)
    environment = fields.Selection(
        string="Environment",
        selection=[("test", "Test"), ("dev", "Dev"), ("production", "Production")],
        required=True,
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner", string="Client", required=True
    )
    odoo_version_id = fields.Many2one(
        comodel_name="odoo.version", string="Odoo Version", required=True
    )
    operating_system_id = fields.Many2one(
        comodel_name="operating.system", string="Operating System"
    )
    hosting_type = fields.Selection(
        string="Hosting Type",
        selection=[("local", "Local"), ("cloud", "Cloud")],
        required=False,
    )
    hosting_provider_id = fields.Many2one(
        comodel_name="hosting.provider", string="Hosting provider"
    )
    cpu = fields.Char(string="CPU")
    ram = fields.Integer(string="RAM")
    storage = fields.Integer(string="Storage")
    storage_type = fields.Selection(
        string="Storage Type",
        selection=[("hdd", "HDD"), ("sdd", "SDD"), ("nvme", "NVME"), ("sata", "SATA")],
    )
    backup = fields.Boolean(string="With Backup")
    backup_provided_by = fields.Selection(
        string="Backup provided by",
        selection=[("veganet", "VEGANET"), ("customer", "Customer"), ("host", "Host")],
    )
    backup_type = fields.Selection(
        string="Backup type",
        selection=[("server", "Server"), ("dbf", "DB+Filestore")],
    )
    duration = fields.Integer(string="Data retention period")
    location = fields.Char(string="Backup Location")
    port_number = fields.Integer(default=8069, string="Port number")
    port_redirection = fields.Boolean(string="Port Redirection")
    ip_address = fields.Char(string="IP address")
    ssh_login = fields.Char(string="SSH login")
    ssh_pwd = fields.Char(string="SSH Password")
    vpn = fields.Boolean(string="Via VPN")

    vpn_type_id = fields.Many2one(comodel_name="vpn.type", string="VPN Type")

    vpn_login = fields.Char(string="VPN login")
    vpn_pwd = fields.Char(string="VPN Password")
    vpn_file = fields.Binary(string="VPN file")
    odoo_url = fields.Char(string="Odoo URL")
    odoo_login = fields.Char(string="Odoo login")
    odoo_pwd = fields.Char(string="Odoo Password ")
    master_pwd = fields.Char(string="Master Password")

    db_login = fields.Char(string="Database login")
    db_pwd = fields.Char(string="Database password")
    multi_company = fields.Boolean(string="Multi Company")
    companies_number = fields.Integer(string="Companies number")
    state = fields.Selection(
        string="State",
        selection=[("draft", "Draft"), ("working", "Working"), ("stopped", "Stopped")],
        default="draft",
    )
    ping_status = fields.Selection(
        string="Ping status",
        selection=[("ok", "OK"), ("nok", "NOK")],
    )

    restart = fields.Char(string="Restart command")
    path = fields.Char(string="Module Path")
    log_command = fields.Char(string="Log command")
    project_id = fields.Many2one(string="Project", comodel_name="project.project")
    hr_employee_id = fields.Many2one(string="Installed by", comodel_name="hr.employee")
    installed_on = fields.Datetime(string="Installed on")
    show_password = fields.Boolean(string="Show Password", default=False, store=True)

    @check_identity
    def toggle_password_visibility(self):
        for record in self:
            record.show_password = True

    def cron_ping_ip_address(self):
        instance_ids = self.env['cloud.instance'].search([("state", '=', "working")])
        for instance in instance_ids:
            try:
                # Run the ping command
                subprocess.run(["ping", instance.ip_address], check=True)
                # subprocess.run(["ping", "-c", "4", instance.ip_address], check=True)
                # If the command runs successfully, return True
                instance.ping_status = 'ok'
            except subprocess.CalledProcessError:
                # If the command returns a non-zero exit code, return False
                instance.ping_status = 'nok'

    # @api.onchange("ping_status")
    def send_mail(self):
        if self.ping_status == "nok":
            mail_template = self.env.ref(
                "v__cloud_instances_manager.ping_notice_mail_template"
            )
            mail_template.send_mail()