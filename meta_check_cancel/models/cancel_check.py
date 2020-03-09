# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class cancel_check(models.Model):
    _name = "cancel.check"
    _description = "Cancel Check Methods"
    _order = 'cancel_date asc'

    cancel_check_no = fields.Char(string="Check Number")
    cancel_check_bank_name = fields.Char(string="Bank Name")
    cancel_check_acc_no = fields.Char(string="Bank Account No")
    cancel_check_amount = fields.Float(string="Check Amount")

    cancel_check_print_date = fields.Char(string="Check Print Date")
    cancel_check_recv_date = fields.Char(string="Check Receive Date")
    cancel_check_reason = fields.Char(string="Void Reason")

    cancel_check_type = fields.Char(string="Check Type")
    cancel_check_payment_type = fields.Char(string="Payment Type")
    
    cancel_check_part_name = fields.Char(string="Partner")
    payment_memo_number = fields.Char(string="Memo Number")

    cancel_date = fields.Date(string='Cancel Date', default=fields.Date.context_today)

    # state = fields.Selection([('draft', 'Draft'), ('posted', 'Validated')], readonly=True, default='draft', copy=False, string="Status")


class acount_payment(models.Model):
    _inherit = "account.payment"
    _description = "Acount Payment Check"

    pdf_viewer = fields.Binary(string="Export Pdf")


    def print_checks_cancel(self):
        if self.void_status == False:
            raise UserError(_("Please Write The Check Void Reason"))
        else:
            checks_number = self.check_number_show
            banks_name = self.bank_account_name.name
            banks_acount_no = self.bank_account_no.acc_number
            amount_check = float(self.amount)
            checks_print_date = self.print_show_date
            checks_recive_date = self.receive_check_date
            checks_cancel_reason = self.all_void_status_reason
            checks_type = self.check_type
            checks_payment_type = self.check_status
            partner_name = self.partner_id.name
            memo = self.communication
            
            payments = self.env['cancel.check'].browse(self.env.context.get('active_ids', []))
            payments.create({'cancel_check_no': checks_number, 'cancel_check_bank_name': banks_name, 'cancel_check_acc_no': banks_acount_no, 
                                'cancel_check_amount': amount_check, 'cancel_check_print_date': checks_print_date, 'cancel_check_recv_date': checks_recive_date,
                                'cancel_check_reason': checks_cancel_reason, 'cancel_check_type': checks_type, 'cancel_check_payment_type': checks_payment_type, 
                                'cancel_check_part_name': partner_name, 'payment_memo_number': memo,})
            for payment in payments:
                payment.check_amount = "check_amount_word"
            return self.write({'state': 'posted', 'void_status': False})
    
    def receive_checks_cancel(self):
        if self.receive_void_status == False:
            raise UserError(_("Please Write The Check Void Reason"))
        else:
            checks_number = self.check_number_show
            banks_name = self.bank_account_name.name
            banks_acount_no = self.bank_account_no.acc_number
            amount_check = float(self.amount)
            checks_print_date = self.print_show_date
            checks_recive_date = self.receive_check_date
            checks_cancel_reason = self.all_void_status_reason
            checks_type = self.check_type
            checks_payment_type = self.check_status
            partner_name = self.partner_id.name
            memo = self.communication
            
            payments = self.env['cancel.check'].browse(self.env.context.get('active_ids', []))
            payments.create({'cancel_check_no': checks_number, 'cancel_check_bank_name': banks_name, 'cancel_check_acc_no': banks_acount_no, 
                                'cancel_check_amount': amount_check, 'cancel_check_print_date': checks_print_date, 'cancel_check_recv_date': checks_recive_date,
                                'cancel_check_reason': checks_cancel_reason, 'cancel_check_type': checks_type, 'cancel_check_payment_type': checks_payment_type, 
                                'cancel_check_part_name': partner_name, 'payment_memo_number': memo,})
            for payment in payments:
                payment.check_amount = "check_amount_word"
            return self.write({'receive_check_number': ' ', 'receive_void_status': False})
            
    
   

