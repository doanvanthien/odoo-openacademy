# -*- coding: utf-8 -*-
import requests

from odoo import http
from odoo.http import request
# from . import service

import json

token = "62f5e2acbeaab21d947f0fe18214359a7db45183o1687942761"

class Controllers(http.Controller):
    # @http.route('/web/session/get_session_infor', type='http', auth ='none')
    # def get_session_infor(self):
    #     request.session.check_security()
    #     request.uid = request.session.uid
    #     request.disable_db = False
    #     return request.env['ir.http'].session_info()
    #
    #
    # @http.route('/web/session/authenticate',auth='none',type='http', scrf=False)
    # def authenticate(self, **kwargs):
    #     request.session.authenticate(kwargs.get('db'),kwargs.get('username'),kwargs.get('password'))
    #     return json.dumps(request.env['ir.http'].session_info())

    @http.route('/api/insert', auth='user', type='json')
    def insert_course(self, **kw):
        if kw.get("token") == token:
            courses = request.env['course'].sudo().create({
                'title':kw.get('title'),
                'description':kw.get('description'),
                'time':kw.get('time'),
            }).id
            return json.dumps(courses)
        return 'invalid token'

    @http.route('/api/search/course', auth='public', type='json')
    def search_course_by_time(self,**kwargs):
        if kwargs.get("token") == token:
            try:
                cr = request.env.cr
                query = """
                select id, title,description, time from course where time is null or time <= %d"""%int(kwargs.get('time'))
                cr.execute(query)
                courses = cr.dictfetchall()
                print(courses)
                return json.dumps(courses)
            except:
                return 'fail'
        return 'invalid token'


    @http.route('/api/delete',auth='user',type='json')
    def delete_course(self,**kwargs):
        if kwargs.get("token") == token:
            try:
                courses = request.env['course'].sudo().search([('id', '=', int(kwargs.get('id')))],
                                                                   []).unlink()
                return 'success'
            except:
                return 'fail'
        return 'invalid token'

    @http.route('/api/update',auth='user',type = 'json')
    def update_course(self,**kwargs):
        if kwargs.get("token") == token:
            try:
                courses = request.env['course'].sudo().search([('id', '=', int(kwargs.get('id')))],
                                                                   []).write({
                    'title': kwargs.get('title'),
                    'description': kwargs.get('description'),
                    'time': kwargs.get('time'),
                })
                print(courses)
                return 'done'
            except:
                return 'fail'
        return 'invalid token'



