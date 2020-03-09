{
    'name': 'Meta Payment Check',  
    'summary': 'Printed the Meta Payment Check',
    'author': 'Metamorphosis Software Solutions',
    'license': 'AGPL-3',
    'website': 'http://odoo.metamorphosis.com.bd/',
    'category': 'account',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'account', 'account_check_printing',
    ],
    'data': [
        
        # 'views/product_bar_view.xml',
        'views/account_payment_check_button.xml',
        'views/check_print_css.xml',
        'views/print_check_wizard_view.xml',
        'views/payment_check_register_view.xml',
        'reports/report.xml',
        'reports/payment_report.xml',
        'views/check_number_search_view.xml',
        # 'views/account_payment_approval_view.xml',invoice_bill_state_view 
        # 'security/bill_approval_security.xml'
        
    ],
    'installable': True,
}