from datetime import date
from odoo import api, fields, models


class CrmCustomerRequest(models.Model):
    _name = "crm.customer.request"
    _description = "request customer"
    _rec_name = "id"

    product_id = fields.Many2one("product.template", string="Product", required=True)

    opportunity_id = fields.Many2one("crm.lead", string="Opportunities", required=True,
                                     domain="[('type', '=', 'opportunity')]")

    date = fields.Date(string="Date", default=date.today(), required=True)

    quantity = fields.Float(string="Quantity", required=True, default=1)
