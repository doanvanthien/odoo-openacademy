import datetime

from odoo import http
from odoo.http import request

token = "62f5e2acbeaab21d947f0fe18214359a7db45183o1687942761"


class Api(http.Controller):

    @http.route('/api/insert_lead', auth='public', type='json')
    def insert_lead(self, **kwargs):
        if kwargs.get('token') == token:
            try:
                vals = kwargs.get('request_ids')
                request.env['crm.lead'].sudo().create({
                    'name': kwargs.get('name'),
                    'partner_id': kwargs.get('partner_id'),
                    'date_deadline': datetime.datetime.strptime(kwargs.get('date_deadline'), "%Y-%m-%d"),
                    'email_from': kwargs.get('email_from'),
                    'phone': kwargs.get('phone'),
                    'description': kwargs.get('description'),
                    'type': 'opportunity',
                    'request_ids': [(0, 0, val) for val in vals]

                })
                return 'done'
            except:
                 return 'false'

        else:
            return 'token invalid'
