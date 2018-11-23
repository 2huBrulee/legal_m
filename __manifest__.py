# -*- coding: utf-8 -*-
{
    'name': "Módulo Legal",

    'summary': """
        Módulo Legal del ODOO""",

    'description': """
        Módulo Legal del ODOO
    """,

    'author': "Grupo 5",
    'website': "sistemas.unmsm.edu.pe",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/reportequeja_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}