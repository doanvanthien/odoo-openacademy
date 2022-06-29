from odoo import api,models, fields

class Course(models.Model):
    _name = 'course'
    _description = 'A course and description'
    _rec_name = 'title'

    title = fields.Char(string = "Title", required = True, index=True)
    description = fields.Char(string = "Description")
    time = fields.Integer(string="Time")

    session_ids = fields.One2many('session','course_id',string="Session IDs")







