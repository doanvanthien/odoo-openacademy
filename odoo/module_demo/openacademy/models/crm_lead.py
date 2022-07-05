from odoo import api,fields,models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    course = fields.Many2one('course',string='Course',ondelete="set null")
    expected_revenue = fields.Monetary(compute='_expected_revenue', readonly = False)

    @api.depends('course')
    def _expected_revenue(self):
        for record in self:
            record.expected_revenue = record.course.price


