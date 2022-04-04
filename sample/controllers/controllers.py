# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Website(http.Controller):
    @http.route('/qtech', website=True, auth='public')
    def run_qtech(self):
        return request.render("sample.sample_page", {})