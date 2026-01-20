from odoo import http
from odoo.http import request

class ParakarsaWebsite(http.Controller):

    @http.route("/", auth="public", website=True)
    def home(self):
        return request.render("parakarsa.landing_page")
