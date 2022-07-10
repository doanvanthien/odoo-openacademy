import base64
import datetime

import xlrd

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many("crm.customer.request", "opportunity_id", string="Requests")

    total_sales = fields.Float(compute='_compute_total_sales', string="Sales", default=0, store=True)

    expected_revenue = fields.Monetary(compute='_onchange_expected_revenue')

    xls_file = fields.Binary('File')

    document_name = fields.Char(string="File Name")

    @api.depends('request_ids')
    def _compute_total_sales(self):
        total = 0
        for request in self.request_ids:
            total += request.quantity
        self.total_sales = total

    @api.onchange('request_ids')
    def _onchange_expected_revenue(self):
        total = 0
        for request in self.request_ids:
            total += (request.quantity
                      * request.product_id.list_price)
        self.expected_revenue = total

    @api.model
    def action_new_quotation(self):
        res = super(CrmLead, self).action_new_quotation()
        vals = []
        for request in self.request_ids:
            vals.append({
                'product_id': request.product_id.id,
                'name': request.product_id.name,
                'product_uom_qty': request.quantity,
                'price_unit': request.product_id.list_price,
                'price_subtotal': request.quantity * request.product_id.list_price
            })

        res['context'].update({
            'default_order_line': [(0, 0, val) for val in vals]
        })
        return res

    @api.onchange('xls_file')
    def import_request(self):
        if self.xls_file:
            self.request_ids = [(5, 0, 0)]
            wb = xlrd.open_workbook(file_contents=base64.decodestring(self.xls_file))
            for sheet in wb.sheets():
                for row in range(1, sheet.nrows):
                    request = []
                    for col in range(sheet.ncols):
                        request.append(sheet.cell(row, col).value)
                    print(request)
                    self.request_ids = [(0, 0, {
                        "product_id": int(request[0]),
                        "date": datetime.datetime.strptime(request[1], "%Y-%m-%d"),
                        "quantity": request[2]
                    })]
