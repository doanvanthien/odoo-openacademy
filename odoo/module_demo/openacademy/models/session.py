from odoo import api,models,fields
from datetime import date
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'session'
    _description = 'Session of course'
    _rec_name = 'id'

    name = fields.Char(string="Name")
    start_date = fields.Datetime(string="Start Date" , default= date.today())
    duration = fields.Integer(string="Duration")
    numbers_of_seats = fields.Integer(string="A number of seats")
    active = fields.Boolean(string="Active",default = True)

    course_id = fields.Many2one('course',string ='Course',required=True,ondelete='restrict')

    attendees_ids = fields.Many2many('attendees',string='Attendees')

    instructor_id = fields.Many2one('attendees',string='Instructor',domain="[('instructor','=',True)]")

    percentage = fields.Float(compute='_compute_percentage')

    @api.depends('attendees_ids')
    def _compute_percentage(self):
        for record in self:
            record.percentage= (len(record.attendees_ids)/record.numbers_of_seats)*100

    @api.onchange('attendees_ids','numbers_of_seats')
    def _onchange_attendees(self):
        if len(self.attendees_ids) > self.numbers_of_seats:
            return {
                'warning':{
                    'title': 'Wrong',
                    'message': 'Full seat'
                }
            }

    @api.constrains('instructor_id','attendees_ids')
    def _check_attendees(self):
        for record in self:
            if record.instructor_id.id in [x.id for x in record.attendees_ids] :
                raise ValidationError('attendee and instructor invalid')









