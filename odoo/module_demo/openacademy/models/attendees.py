from odoo import models,fields

class Attendees(models.Model):
    _name = 'attendees'
    _description = 'people attend session'
    _rec_name = 'id'

    name = fields.Char(string="Name")

    session_ids = fields.Many2many('session',string='Session IDs')

class Partner(models.Model):
    _name = 'partner'
    _description = 'instructor'
    _inherit = 'attendees'

    instructor = fields.Boolean(string = 'Instructor')

    def name_get(self):
        res=[]
        for record in self:
            res.append((record.id, "{} {}".format(record.id,record.name)))
        return res