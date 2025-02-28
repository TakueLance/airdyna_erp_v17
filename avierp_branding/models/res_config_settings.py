from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_system_name = fields.Char('System Name', help="Setup System Name,which replace Odoo")    
    app_documentation_url = fields.Char('Documentation Url')    
    app_support_url = fields.Char('Support Url')    

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        app_system_name = ir_config.get_param('app_system_name', default='AirDyna')
        app_documentation_url = ir_config.get_param('app_documentation_url',
                                                    default='https://www.airdyna.co.zw')        
        app_support_url = ir_config.get_param('app_support_url', default='https://airdyna.co.zw')             
        res.update(
            app_system_name=app_system_name,
            app_documentation_url=app_documentation_url,
            app_support_url=app_support_url,
        )        
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ir_config = self.env['ir.config_parameter'].sudo()
        ir_config.set_param("app_system_name", self.app_system_name or "")
        ir_config.set_param("app_documentation_url", self.app_documentation_url or "https://www.airdyna.co.zw")
        ir_config.set_param("app_support_url", self.app_support_url or "https://www.airdyna.co.zw")        