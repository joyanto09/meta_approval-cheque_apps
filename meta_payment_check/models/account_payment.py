# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words
from datetime import datetime

class AccountPaymentCheck(models.Model):

    _inherit = 'account.payment'
    
    check_number_seq = fields.Char(string='Check Number', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    
    amount_words = fields.Char(string="Amount Words")
    bank_account_no = fields.Many2one('res.partner.bank', related='journal_id.bank_account_id', string='Bank Account No', readonly=True)
    bank_account_name = fields.Many2one('res.bank', related='journal_id.bank_id', string='Bank Name', readonly=True)
    
    first_date = fields.Char(string="First Date")
    print_show_date = fields.Char(string="Check Print Date", readonly=True)
    
    first_charecter_year = fields.Char(string="Year Char First")
    second_charecter_year = fields.Char(string="Year Char second")
    third_charecter_year = fields.Char(string="Year Char Third")
    fourth_charecter_year = fields.Char(string="Year Char Fourth")
    
    first_charecter_month = fields.Char(string="Month Char First")
    second_charecter_month = fields.Char(string="Month Char second")
    
    first_charecter_day = fields.Char(string="Day Char First")
    second_charecter_day = fields.Char(string="Day Char second")
    
    receive_cash = fields.Boolean(string='Receive Cash')
    receive_check_number = fields.Char(string="Receive Check Number")
    receive_check_date = fields.Date(string="Receive Check Date")
    check_status = fields.Char(string="Status")
    # <!--25-01-2020-->
    check_amount = fields.Integer(string="Check Amount")
    check_amount2 = fields.Char(string="Amount2")
    check_amount_word = fields.Char(string="Amount in Words")
    check_currency = fields.Char(string="Currency Word")
    # <!--end-->
    check_number_show = fields.Char(string="Check Number Show", )
    check_type = fields.Selection([('CDC', 'CDC'), ('CD', 'CD')], default='', copy=False, string="Check Type")

    receive_void_status = fields.Boolean(string='Void', default=False)
    receive_void_status_reason = fields.Text(string='Void Reason')
    all_void_status_reason = fields.Char(string='Void Reason')
    reacivie_print_date = fields.Char(string="Check Date")

    check_pay_order = fields.Boolean(string='Pay Order', default=False)
    check_pay_order_details = fields.Char(string='Pay Order Details', default=False)
    
    @api.onchange('amount')
    def amount_to_words(self):
        if self.company_id:
            self.amount_words = num2words(self.amount)
            
    @api.model
    def create(self, vals):

        vals['amount_words'] = vals['amount_words'].title()
        
        return super(AccountPaymentCheck, self).create(vals)
    
    # @api.depends('print_show_date')
    # def get_date(self):
    #     date = self.print_show_date
        
    #     self.first_date = date
        
        
    # @api.onchange('first_date')
    # def get_date_char(self):
    #     date2 = self.first_date
        
    #     self.first_charecter_year = (date2[0])
    #     self.second_charecter_year = (date2[1])
    #     self.third_charecter_year = (date2[2])
    #     self.fourth_charecter_year = (date2[3])
    #     self.first_charecter_month = (date2[5])
    #     self.second_charecter_month = (date2[6])
    #     self.first_charecter_day = (date2[8])
    #     self.second_charecter_day = (date2[9])
        
    get_amount = fields.Float(string="Amounts", compute="get_amounts")
    
    @api.depends('amount')
    def get_amounts(self):
        amounts = self.amount
        
        self.get_amount = amounts
        
    void_status = fields.Boolean(string='Void', default=False)
    void_status_reason = fields.Text(string='Void Reason')
    
    
    def cancel_check(self):
        if self.void_status == False:
            raise UserError(_("Please Write The Void Reason"))
        else:
            return self.write({'state': 'cancelled'})
    
    
    @api.onchange('journal_id')
    def _compute_hide_receive_payment(self):
        for payment in self:
            if payment.journal_id.type in ['cash']:
                payment.receive_cash = True
            else:
                payment.receive_cash = False

    @api.onchange('payment_type')
    def change_status(self):
        for payment in self:
            if payment.payment_type in ['outbound']:
                payment.check_status = 'Vendor Payment'
            elif payment.payment_type in ['inbound']:
                payment.check_status = 'Customer Payment'
            else:
                payment.check_status = ' '
                
    @api.onchange('amount')
    def get_check_amounts(self):
        check_amounts = self.amount
        
        self.check_amount = check_amounts
        
    @api.onchange('check_amount')
    def get_total_amounts(self):
        check_total_amounts = int(self.check_amount)
        
        self.check_amount2 = check_total_amounts
        
    @api.onchange('check_amount2')
    def get_amounts_words(self):
        number = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
        nty = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        tens = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        
        check_amounts_number = int(self.check_amount2)
        
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
                
    @api.onchange('currency_id')
    def _currency_word(self):
        check_curr = self.currency_id.currency_unit_label
        
        self.check_currency = check_curr
    
    @api.onchange('receive_check_number')
    def _check_number_show(self):
        check_num2 = self.receive_check_number
        
        self.check_number_show = check_num2
        
    @api.onchange('void_status_reason')
    def _print_void_reason(self):
        void_satus1 = self.void_status_reason

        self.all_void_status_reason = void_satus1

    @api.onchange('receive_void_status_reason')
    def _receive_void_reason(self):
        void_satus2 = self.receive_void_status_reason
        
        self.all_void_status_reason = void_satus2
    #     self.check_number_show = check_num2

    @api.onchange('receive_check_date')
    def _receive_and_print_check_date(self):

        self.reacivie_print_date = self.receive_check_date

    @api.onchange('check_pay_order')
    def _pay_order_details(self):

        if self.check_pay_order == True:
            self.check_pay_order_details = "Issue Pay Order to- "

        else:
             self.check_pay_order_details = " "  
        
            
            
        # self.check_amount_word = check_amounts_words % 10
                
    