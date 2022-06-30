from odoo import api,fields,models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    course = fields.Many2one('course',string='Course',ondelete="set null")