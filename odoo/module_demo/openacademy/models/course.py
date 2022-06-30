from odoo import api,models, fields
from odoo.exceptions import ValidationError

class Course(models.Model):
    _name = 'course'
    _description = 'A course and description'
    _rec_name = 'title'

    title = fields.Char(string = "Title", required = True, index=True)
    description = fields.Char(string = "Description")
    time = fields.Integer(string="Time")

    session_ids = fields.One2many('session','course_id',string="Session IDs")

    @api.constrains('title','description')
    def _check_title_description(self):
        for record in self:
            if record.title == record.description:
                raise ValidationError('title has to different from description')

    @api.constrains('title')
    def _check_unique_title(self):
            count_record = self.search_count([('title','=',self.title),('id','!=',self.id)])
            if count_record > 0:
                raise ValidationError('title is existing')










