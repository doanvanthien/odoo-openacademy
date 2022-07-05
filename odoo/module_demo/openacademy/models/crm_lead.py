from odoo import api,fields,models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    course = fields.Many2one('course',string='Course',ondelete="set null")
    expected_revenue = fields.Monetary(readonly = False)

    @api.onchange('course')
    def _expected_revenue(self):
        self.expected_revenue = self.course.price


