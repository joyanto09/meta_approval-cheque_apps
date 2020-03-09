# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class DashBoard(models.Model):
    _name = "dash.board"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    # _inherits = ['purchase.order']

    name = fields.Char(string="Name", default="Approval")

    # Purchase Approval
    def open_purchase_first_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
            'target' : 'current',
        }


    def open_purchase_second_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_purchase_third_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_purchase_fourth_approval_list(self):

        return {
            'name': _('Purchase'),
            'domain': [('state', '=', 'fourth_approval')],
            'res_model': 'purchase.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    # Sales Approval
    def open_sales_first_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_sales_second_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_sales_third_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_sales_fourth_approval_list(self):

        return {
            'name': _('Sales'),
            'domain': [('state', '=', 'fourth_approval')],
            'res_model': 'sale.order',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    

    # Payments Approval
    def open_payments_first_approval_list(self):

        return {
            'name': _('Payments'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'account.payment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_payments_second_approval_list(self):

        return {
            'name': _('Payments'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'account.payment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_payments_third_approval_list(self):

        return {
            'name': _('Payments'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'account.payment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    
    # Journal Approval
    def open_journal_first_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'first_approval')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
    
    def open_journal_second_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'second_approval')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    def open_journal_third_approval_list(self):

        return {
            'name': _('Journal'),
            'domain': [('state', '=', 'third_approval')],
            'res_model': 'account.move',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }


   
