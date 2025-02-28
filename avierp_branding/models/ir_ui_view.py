from odoo import api, fields, models, _
from odoo.exceptions import UserError

class View(models.Model):
    _inherit = 'ir.ui.view'

    def _render_template(self, template, values=None):        
        if not values:
            values = {}
        values["title"] = values["app_title"] = self.env['ir.config_parameter'].sudo().get_param("app_system_name", "AirDyna")        
        return super(View, self)._render_template(template, values=values)