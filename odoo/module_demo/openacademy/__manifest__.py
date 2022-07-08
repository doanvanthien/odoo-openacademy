# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'crm',
                'mail',
                ],

    # always loaded
    'data': [
        'security/openacademy_sercurity.xml',
        'security/ir.model.access.csv',
        'views/attendees_view.xml',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/course_menu_view.xml',
        'views/crm_lead_views.xml',
        'report/session_card.xml',
        'wizard/add_attendee_view.xml',

    ],
    'assets':{
        'web.assets_backend':  [
            'openacademy/static/src/js/demo_widget.js',
        ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/course_demo.xml',
    ],
    'license': 'LGPL-3',
}
