# -*- coding: utf-8 -*-
{
    'name': "Razorpay Payment",

    'summary': """
        Razorpay payment""",

    'description': """
        Razorpay payment
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'khra_yelo_orders'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/razorpay_configuration_views.xml',
        'views/views.xml',
        'views/razorpay_settlement_views.xml',
        'views/templates.xml',
        'data/razorpay_data.xml',
        'wizard/razorpay_settlement_compute_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
