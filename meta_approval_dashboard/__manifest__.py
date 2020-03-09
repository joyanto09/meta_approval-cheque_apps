{
    'name': 'Approval Dashboard',  
    'summary': 'Approval For All Users',
    'author': 'Metamorphosis Software Solutions',
    'license': 'AGPL-3',
    'website': 'https://metakave.com/',
    'category': 'Apps',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'mail', 'purchase', 'account',
    ],
    'data': [
        
        'security/ir.model.access.csv',
        'views/approval_dashboard_view.xml',
        # 'backend_assets.xml',
        
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}