{
    'name': 'Meta Sales Approval',  
    'summary': ''' 
            Apps will create Approval For Sales Order 
        ''',
    "description": """This module will create multi-level Approval For Sales Order""",
    'author': 'Metamorphosis',
    'company': 'Metamorphosis Limited',
    'license': 'AGPL-3',
    'website': 'http://metamorphosis.com.bd/',
    'category': 'Sale',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base', 'sale', 'mail',
    ],
    'data': [
        
        'security/sale_security.xml',
        'views/sale_view.xml',
        
    ],
    'icon': "/meta_sale_approval/static/description/icon.png",
    "images": ["static/description/baner.png"],
    'installable': True,
    "auto_install": False,
    'price':99.0,
    'currency':'EUR',
}