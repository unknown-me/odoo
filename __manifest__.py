# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': """
        Simple hospital management app""",

    'description': """
        only for hospital management
    """,

    'author': "Chetan Dua",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'HealthCare',
    'version': '0.1',

    # any module necessary for this one to work correctly
    #'depends': ['base'],

    # always loaded
    'data': [
        'masterData.xml',
        'security/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/staff_views.xml',
        'views/patient_views.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/staff_id_sequence.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
