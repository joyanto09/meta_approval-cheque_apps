# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict

from datetime import datetime


class acount_jurnal(models.Model):
    _inherit = "account.move"
    _description = "Jurnal Check Details"

    amount_check = fields.Integer(string="Amount", compute="_cheange_amount")
    amount_check2 = fields.Char(string="Amount 2", compute="get_total_amounts")
    amount_check3 = fields.Float(string="Amount 3", compute="check_print_amount")
    check_amount_word = fields.Char(string="Amount in Words", compute="get_amounts_words")
    get_print_date = fields.Char(string="Get Date")

    journal_check = fields.Boolean(string="Check", default=False)
    journal_check_type = fields.Selection([('CDC', 'CDC'), ('CD', 'CD')], default='', copy=False, string="Check Type")
    hide_print_button  = fields.Boolean(string="Hide Print Button", compute="show_cancels_button")
    journal_payment_cash  = fields.Boolean(string="Payment Cash", default=False)

    first_charecter_year = fields.Char(string="Year Char First")
    second_charecter_year = fields.Char(string="Year Char second")
    third_charecter_year = fields.Char(string="Year Char Third")
    fourth_charecter_year = fields.Char(string="Year Char Fourth")
    
    first_charecter_month = fields.Char(string="Month Char First")
    second_charecter_month = fields.Char(string="Month Char second")
    
    first_charecter_day = fields.Char(string="Day Char First")
    second_charecter_day = fields.Char(string="Day Char second")
    journal_check_number = fields.Char(string="Check Number")

    journal_void_status = fields.Boolean(string="Void")
    journal_hide_void_status = fields.Boolean(string="Void Status")
    journal_void_status_reason = fields.Text(string="Void Reason")

    check_pay_order = fields.Boolean(string='Pay Order', default=False)
    check_pay_order_details = fields.Char(string='Pay Order Details', default=False)

    @api.depends('amount_total')
    def _cheange_amount(self):

        amount = int(self.amount_total)
        self.amount_check = amount

    @api.depends('amount_check')
    def get_total_amounts(self):
        check_total_amounts = int(self.amount_check)
        
        self.amount_check2 = check_total_amounts

    @api.depends('amount_check2')
    def get_amounts_words(self):
        number = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        nty = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        tens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        
        check_amounts_number = int(self.amount_check2)
        
        if check_amounts_number > 999999999999:
            # raise UserError(_('The Ammount is more then 12 digit'))
            self.check_amount_word = "The Amount Limit is More Then of 12-digits"
        
        elif check_amounts_number == 0:
            self.check_amount_word = "Zero Taka"
            
        else:
            d = [0,0,0,0,0,0,0,0,0,0,0,0]
            i = 0
            
            while check_amounts_number > 0:
                d[i] = check_amounts_number % 10
                i += 1
                check_amounts_number = check_amounts_number // 10
            num = ''
            
            if d[11] != 0:
                if (d[11] == 1):
                    num += tens[d[10]]+ " Thousand "
                else:
                    num += nty[d[11]]+" "+number[d[10]]+ " Thousand "
            else:
                if d[10] != 0:
                    num += number[d[10]]+ " Thousand "

            if d[9] != 0:
                    num += number[d[9]]+ " Hundred "

            if d[8] != 0:
                if (d[8] == 1):
                    num += tens[d[7]]+ " Crore "
                else:
                    num += nty[d[8]]+" "+number[d[7]]+ " Crore "
            else:
                if d[7] != 0:
                    num += number[d[7]]+ " Crore "

            if d[6] != 0:
                if (d[6] == 1):
                    num += tens[d[5]]+ " Lac "
                else:
                    num += nty[d[6]]+" "+number[d[5]]+ " Lac "
            else:
                if d[5] != 0:
                    num += number[d[5]]+ " Lac "
            
            if d[4] != 0:
                if (d[4] == 1):
                    num += tens[d[3]]+ " Thousand "
                else:
                    num += nty[d[4]]+" "+number[d[3]]+ " Thousand "
            else:
                if d[3] != 0:
                    num += number[d[3]]+ " Thousand "
            
            if d[2] != 0:
                num += number[d[2]]+ " Hundred "
            
            if d[1] != 0:
                if (d[1] == 1):
                    num += tens[d[0]]
                else:
                    num += nty[d[1]]+" "+number[d[0]]
            else:
                if d[0] != 0:
                    num += number[d[0]]

            self.check_amount_word = num


    def print_checks_journal_bd(self):
        
        return {
            'name': _('Print Journal Checks'),
            'type': 'ir.actions.act_window',
            'res_model': 'print.journal.checks',
            'view_mode': 'form',
            'target': 'new',
            # 'context': {
            #     'payment_ids': self.ids,
            #     'default_next_check_number': next_check_number,
            # }
        }

    @api.depends('amount_total')
    def check_print_amount(self):

        amount_print_check = self.amount_total
        self.amount_check3 = amount_print_check


    @api.onchange('journal_id')
    def _compute_hide_receive_payment(self):
        for payment in self:
            if payment.journal_id.type in ['cash']:
                payment.journal_payment_cash = True
            else:
                payment.journal_payment_cash = False

    @api.onchange('journal_id')
    def _compute_hide_pritn_receive_payment(self):
        for payment in self:
            if payment.journal_id.type in ['cash']:
                payment.journal_check = False
            else:
                payment.journal_check = True
    
    @api.depends('journal_check')
    def show_cancels_button(self):
        if (self.journal_check == False):
            self.hide_print_button = True

        elif (self.journal_check == True):
            self.hide_print_button = False


    def print_checks_cancel(self):
        if self.journal_void_status == False:
            raise UserError(_("Please Write The Check Void Reason"))
        else:
            checks_number = self.journal_check_number
            banks_name = self.journal_id.name
            amount_check = self.amount_check3
            checks_print_date = self.get_print_date
            checks_cancel_reason = self.journal_void_status_reason
            checks_type = self.journal_check_type
            partner_name = self.partner_id.name
            
            payments = self.env['cancel.check'].browse(self.env.context.get('active_ids', []))
            payments.create({'cancel_check_no': checks_number, 'cancel_check_bank_name': banks_name, 'cancel_check_amount': amount_check, 
                                'cancel_check_print_date': checks_print_date, 
                                'cancel_check_reason': checks_cancel_reason, 'cancel_check_type': checks_type, 'cancel_check_part_name': partner_name,})
            for payment in payments:
                payment.check_amount = "check_amount_word"
            return self.write({'journal_check': True, 'journal_check_number': ''})
    
    @api.onchange('check_pay_order')
    def _pay_order_details(self):

        if self.check_pay_order == True:
            self.check_pay_order_details = "Issue Pay Order to- "

        else:
             self.check_pay_order_details = " "



class acount_jurnal_lines(models.Model):
    _inherit = "account.move.line"
    _description = "Jurnal Check Details line"


    # @api.onchange('partner_id')
    # def _cheange_amount(self):

    #     amount = self.partner_id.name
    #     payments = self.env['account.move'].browse(self.env.context.get('active_ids', []))

    #     payments.journal_name = amount


    # @api.depends('hide_print_button', 'journal_check')
    # def show_cancel_button(self):
    #     if (self.journal_check == False):
    #         self.hide_print_button = True

    #     elif (self.journal_check == True):
    #         self.hide_print_button = False

    