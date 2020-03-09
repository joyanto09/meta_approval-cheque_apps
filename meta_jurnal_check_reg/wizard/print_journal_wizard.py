# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words
from datetime import datetime

class print_journal_wizard(models.TransientModel):
    _name = "print.journal.checks"
    
    check_print_date = fields.Date(string="Print Check Date", default=fields.Date.context_today)
    next_check_number = fields.Char('Next Check Number', required=True)
    
    def print_journal_checks_bd(self):
        check_number = int(self.next_check_number)
        check_date = str(self.check_print_date)
        check_number_check = self.next_check_number
        search_check_num = self.env['account.move'].search([('journal_check_number', '=', check_number_check)])
        if search_check_num:
            raise UserError(_("This Check Number is Used"))
        
        else:
            payments = self.env['account.move'].browse(self.env.context.get('active_ids', []))
            # payments.filtered(lambda r: r.state == 'draft').post()
            payments.filtered(lambda r: r.state not in ('cancelled')).write({'state': 'posted', 'journal_check': False, 'journal_void_status': False})
            for payment in payments:
                payment.journal_check_number = check_number_check
                check_number += 1
                payment.get_print_date = check_date
                payment.first_charecter_year = (check_date[0])
                payment.second_charecter_year = (check_date[1])
                payment.third_charecter_year = (check_date[2])
                payment.fourth_charecter_year = (check_date[3])
                payment.first_charecter_month = (check_date[5])
                payment.second_charecter_month = (check_date[6])
                payment.first_charecter_day = (check_date[8])
                payment.second_charecter_day = (check_date[9])
            return payments.do_print_checks_bd()