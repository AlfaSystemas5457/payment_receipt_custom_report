# -*- coding: utf-8 -*-
{
    'name': "Poliza de pago custom",
    'summary': """Modifica los recibos de pago""",
    'description': """Modifica los recibos de pago""",

    'author': "DGV",
    # 'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': 1,
    'application': True,

    'depends': ['account', 'web', 'cdfi_invoice'],
    
    'data': [
        'views/document_template_boxed_view.xml',
        'views/payment_receipt_view.xml',
        'views/add_field_receipt_view.xml',
        'views/payment_receipt_view_template.xml',
        'views/components_views_template.xml',
    ],
}