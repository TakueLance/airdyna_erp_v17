from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.binary import Binary


class WebBrandingController(Binary):
    @http.route(["/web/image/company_logo"], type="http", auth="user")
    def company_logo2(self, **kw):
        company_id = request.env.company.id or request.env.user.company_id.id
        return self.content_image(model="res.company", id=company_id, field="logo")
