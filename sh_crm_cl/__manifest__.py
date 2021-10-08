# -*- coding: utf-8 -*-
{
    'name': "CRM Leads & Opportunity Checklist",

    "summary": """CRM Leads & Opportunity Checklist,reminder for crm checklist app, make checklist module, crm opportunity checklist, find sub task checklist, remember of important things, crm lead checklist odoo """,
    "description": """This module useful to a list of items required, things to be done, or points to be considered, used as a reminder.
    reminder for crm checklist app, make checklist module, crm checklist for opportunity, find sub task checklist, remember of important things, crm checklist for lead odoo""",

    'author': "Loyal It Solutions PVT LTD",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
