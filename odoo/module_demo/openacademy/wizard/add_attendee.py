from odoo import models, fields

class AddAttendee(models.TransientModel):
    _name = "add.attendee"
    _description = "update more attendee for session model"

    session_id = fields.Many2one("session",string = "Session")
    attendees_ids = fields.Many2many("attendees",string = "Attendees")

    def add_attendees(self):
        ids = self.env.context['active_ids']
        sessions = self.env['session'].browse(ids)
        new_data = {}

        if self.attendees_ids:
            new_data["attendees_ids"] = self.attendees_ids

        sessions.write(new_data)