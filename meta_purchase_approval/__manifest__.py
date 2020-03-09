{
    'name': 'Meta Purchase Approval','summary': ''' 
            Apps will create Approval For Purchase Order 
        ''',
    "description": """This module will create multi-level Approval For Purchase Order""",
    'author': 'Metamorphosis',
    'company': 'Metamorphosis Limited',
    'license': 'AGPL-3',
    'website': 'http://metamorphosis.com.bd/',
    'category': 'Purchase',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'purchase','web', 'mail',
    ],
    'data': [
        
        'security/purchase_security.xml',
        'views/purchase_view.xml',
        # 'backend_assets.xml',
        
    ],
    'icon': "/meta_purchase_approval/static/description/icon.png",
    "images": ["static/description/baner.png"],
    'installable': True,
    "auto_install": False,
    'price':99.0,
    'currency':'EUR',
}