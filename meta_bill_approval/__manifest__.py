{
    'name': 'Meta Bill Approval',  
    'summary': 'Approval For Bill',
    'author': 'Metakave Software Solutions',
    'license': 'AGPL-3',
    'website': 'https://metakave.com/',
    'category': 'Sale',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'sale', 'account', 'mail',
    ],
    'data': [
        
        'security/bill_approval_security.xml',
        'views/bill_approval_view.xml',
        'views/invoice_bill_state_view.xml', 
        # 'views/account_payment_approval_view.xml',invoice_bill_state_view 
        
    ],
    'installable': True,
}