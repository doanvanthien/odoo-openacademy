from odoo import api,models,fields

class Session(models.Model):
    _name = 'session'
    _description = 'Session of course'
    _rec_name = 'id'

    name = fields.Char(string="Name")
    start_date = fields.Datetime(string="Start Date")
    duration = fields.Integer(string="Duration")
    numbers_of_seats = fields.Integer(string="A number of seats")

    course_id = fields.Many2one('course',string ='Course',required=True,ondelete='restrict')

    attendees_ids = fields.Many2many('attendees',string='Attendees', groups='openacademy.group_openacademy_manager')

    partner_id = fields.Many2one('partner',string='Instructor',domain="[('instructor','=',True)]")

    percentage = fields.Float(compute='_compute_percentage')

    @api.depends('attendees_ids')
    def _compute_percentage(self):
        for record in self:
            record.percentage= (len(record.attendees_ids)/record.numbers_of_seats)*100







