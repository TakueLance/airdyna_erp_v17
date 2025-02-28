from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Disable Odoo bot initial message
    def _init_odoobot(self):
        return False

class ResCompany(models.Model):
    _inherit = 'res.company'

    logo_dark = fields.Image('Logo for Dark BG')