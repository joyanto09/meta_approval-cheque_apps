# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class AccountMoveApproval(models.Model):
    
    _inherit = 'account.move'
    
    def open_payment_form_view(self):
        return {
            'name': _('Payments'),
            'domain': [('communication', '=', self.name)],
            'res_model': 'account.payment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
        
        # "view_id": self.env.ref('account.view_account_payment_invoice_form').id,