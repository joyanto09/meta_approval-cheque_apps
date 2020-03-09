{
    'name': 'Meta Cancel Chcks',
    'summary': 'Meta Cancel Check List',
    'author': 'Metamorphosis Software Solutions',
    'license': 'AGPL-3',
    'website': 'http://odoo.metamorphosis.com.bd/',
    'category': 'account',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/cancel_check_view.xml',
        'views/acount_payment_cancel_check_view.xml',
    ],
    'installable': True,
}