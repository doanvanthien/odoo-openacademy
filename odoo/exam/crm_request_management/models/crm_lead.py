from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many("crm.customer.request", "opportunity_id", string="Requests")

    total_sales = fields.Float(compute='_compute_total_sales', string="Sales", default=0, store=True)

    expected_revenue = fields.Monetary(compute='_onchange_expected_revenue')

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
