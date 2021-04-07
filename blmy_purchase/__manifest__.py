
# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Bloomy: Purchase Customization',
    'version': '1.0',
    'category': 'Purchase',
    'sequence': 50,
    'summary': 'Customization for Purchase',
    'depends': ['purchase'],
    'description': """
Purchase Customization
===============
* Add additional fields to vendor
""",
    'data': [
        'views/res_partner_views.xml',
    ],
    'qweb': [
    ],
    'demo': [],
    'application': False,
    'license': 'OEEL-1',
}
