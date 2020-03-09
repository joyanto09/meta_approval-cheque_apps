{
    'name': 'Meta Jurnal Check',  
    'summary': 'Printed Jurnal Payment Check',
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
        
        'views/acount_jurnal_view.xml',
        'wizard/print_jouranl_wizard_view.xml',
        'reports/journal_check_report.xml',
        'reports/report.xml',
        'views/jurnal_check_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
}