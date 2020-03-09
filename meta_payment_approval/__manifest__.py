{
    'name': 'Meta Payment Approval',  
    'summary': 'Meta Payment Approval For Sales and Purchase and Direct Payment',
    'author': 'Metakave Software Solutions',
    'license': 'AGPL-3',
    'website': 'https://metakave.com/',
    'category': 'Purchase',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'purchase', 'account', 'mail',
    ],
    'data': [
        # 'backend_assets.xml',
        # 'security/payment_security.xml',
        'views/payment_invoice_approval_view.xml',
        'views/account_payment_approvl.xml',
        'views/open_payment_view.xml',
        
    ],
    'installable': True,
}