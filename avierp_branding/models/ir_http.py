from odoo import models
from odoo.http import request

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        config_parameter = request.env['ir.config_parameter'].sudo()
        result['app_system_name'] = config_parameter.get_param('app_system_name')
        result['app_documentation_url'] = config_parameter.get_param('app_documentation_url')        
        result['app_support_url'] = config_parameter.get_param('app_support_url')        
        result['app_account_url'] = config_parameter.get_param('app_account_url')
        return result