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

    # @api.constrains('title')
    # def _check_unique_title(self):
    #         count_record = self.search_count([('title','=',self.title),('id','!=',self.id)])
    #         if count_record > 0:
    #             raise ValidationError('title is existing')
    #


    _sql_constraints = [
        ('unique_title','unique (title)','title must be unique')
    ]

class Course(models.Model):
    _inherit = 'course'

    active = fields.Boolean('Active', default=True)
    lead_ids = fields.One2many('crm.lead', 'course', domain=[('type', '=', 'lead')])
    lead_count = fields.Integer(string = 'Lead', default=0, compute= "_lead_count")

    price = fields.Integer(string = 'Price Unit')

    opportunity_ids = fields.One2many('crm.lead','course',domain=[('type','=','opportunity')])
    opportunity_count = fields.Integer(string = 'Opportunity', default = 0, compute ="_opportunity_count")

    @api.depends('lead_ids')
    def _lead_count(self):
        for record in self:
            record.lead_count = len(record.lead_ids)

    @api.depends('opportunity_ids')
    def _opportunity_count(self):
        for record in self:
            record.opportunity_count = len(record.opportunity_ids)

    def action_view_lead(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("crm.crm_lead_all_leads")
        action['domain'] = [('id', 'in', self.lead_ids.ids), ('type', '=', 'lead')]
        action['context'] = dict(self._context, create=False)
        return action

    def action_view_opportunity(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("crm.crm_lead_opportunities")
        action['domain'] = [('id', 'in', self.opportunity_ids.ids), ('type', '=', 'opportunity')]
        action['context'] = dict(self._context, create=True)
        action['context'] = {'default_course':self.id,'default_expected_revenue': self.price,'default_type':'opportunity'}
        return action

    @api.returns('self')
    def copy(self, default=None):
        default = dict(default or {})
        default.update({
            'title': 'Copy of ' + self.title })
        return super(Course, self).copy(default)









