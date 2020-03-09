# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words
from datetime import date

class PaymentCheckRegister(models.Model):
    _name = "payment.check.register"
    # _inherit = 'account.payment'
    
    name = fields.Many2one('account.payment', string='Payment Sequence')
    check_number = fields.Char(related='name.check_number', string='Check Nuber')
    bank_name = fields.Many2one('res.bank', related='name.bank_account_name', string="Bank Name")
    account_number = fields.Many2one('res.partner.bank', related='name.bank_account_no', string="Account Number")
    check_amount = fields.Float(related='name.get_amount', string="Amount")
    amount_words = fields.Char(related='name.check_amount_in_words', string="Amount Words")
    printed_date = fields.Char(related='name.first_date', string='Print Date')
    issued_date = fields.Date(string='Issued Date', default=fields.Date.context_today, required=True, readonly=False, states={'not_issued': [('readonly', False)]}, copy=False, tracking=True)
    cash_out_date = fields.Date(string='Cash Out Date', default=fields.Date.context_today, required=True, readonly=False, states={'issued': [('readonly', False)]}, copy=False, tracking=True)
    state = fields.Selection(selection=[
        ('not_issued', 'Not Issued'),
        ('issued', 'issued'),
        ('void', 'Void')
        ], string='Check Status', required=True, readonly=True, copy=False, tracking=True, default='not_issued')
    
    check_void = fields.Boolean(string='Void', default=False)
    void_reason = fields.Text(string='Void Reason', default=False)
    
    
    # @api.onchange('bank_naem', 'account_number')
    # def check_data(self):
    #     check_num = self.check_number
        
    #     search_date = self.env['account.payment'].search([('check_number', '=', check_num)])
        
    #     if search_date:
    #         self.bank_naem = search_date.bank_account_name
    #         self.account_number = search_date.bank_account_no
    
    
    
    
    # default=fields.Date.context_today, 