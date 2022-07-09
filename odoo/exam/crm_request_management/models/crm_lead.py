from odoo import api,fields,models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    request_ids = fields.One2many("crm.customer.request","opportunity_id",string ="Requests")

    total_sales = fields.Float(compute = '_compute_total_sales', string="Sales" ,default = 0, store = True)

    @api.depends('request_ids')
    def _compute_total_sales(self):
        for record in self:
            total = 0
            for request in record.request_ids.ids:
                total += self.env['crm.customer.request'].search([('id','=',request)]).quantity
            record.total_sales = total

    @api.onchange('request_ids')
    def _compute_expected_revenue(self):
        for record in self:
            total = 0
            for request in record.request_ids.ids:
                total += (self.env['crm.customer.request'].search([('id','=',request)]).quantity
                        * self.env['crm.customer.request'].search([('id','=',request)]).product_id.list_price)

            record.expected_revenue = total

    # @api.model
    # def action_new_quotation(self):
    #     res = super(CrmLead,self).action_new_quotation()
    #     for request in self.request_ids.ids:
    #         vals = {
    #             'product_id': self.env['crm.customer.request'].search([('id', '=', request)]).product_id,
    #             'product_uom_qty': self.env['crm.customer.request'].search([('id','=',request)]).quantity,
    #         }
    #         res['context'].update({
    #             'default_order_line': vals
    #         })
    #     print(res)
    #     return res
