# -*- coding: utf-8 -*-
{
    'name': "projectmandiri",

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
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/negaraasal_view.xml',
        'views/daging_view.xml',
        'views/object_view.xml',
        'views/breeder_view.xml',
        'views/buyer_view.xml',
        'views/perusahaan_view.xml',
        'views/penjualan_view.xml',
        'report/report.xml',
        'views/dagingdatang_view.xml',
        'wizard/dagingdatang_wizard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}