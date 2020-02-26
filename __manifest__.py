{
    "name": "same_motion_module",
    "version": "1.0",
    "category": "Account",
    "website": "www.test.com",
    "author": "Alex Tito",
    "license": "LGPL-3",
    "installable": True,
    "depends": [
        'point_of_sale',
        'contacts',
        'account',
        'account_invoicing',
        'product',
        'crm',
    ],
    "data": [
        'views/templates.xml',
        'views/account_invoice.xml',
        'reports/render.xml',
    ],
    'qweb': [
        'static/src/xml/*',
    ],
}

