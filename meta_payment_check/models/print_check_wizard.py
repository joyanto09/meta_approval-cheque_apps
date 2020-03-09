# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words
from datetime import datetime

class PrintCheckWizard(models.TransientModel):
    _inherit = "print.prenumbered.checks"
    
    check_print_date = fields.Date(string="Print Check Date", default=fields.Date.context_today)
    
    def print_checks_bd(self):
        check_number = int(self.next_check_number)
        check_date = str(self.check_print_date)
        check_number_check = self.next_check_number
        search_check_num = self.env['account.payment'].search([('check_number', '=', check_number_check)])
        if search_check_num:
            raise UserError(_("This Check Number is Used"))
        
        else:
            payments = self.env['account.payment'].browse(self.env.context['payment_ids'])
            payments.filtered(lambda r: r.state == 'draft').post()
            payments.filtered(lambda r: r.state not in ('sent', 'cancelled')).write({'state': 'sent'})
            for payment in payments:
                payment.check_number = check_number
                payment.check_number_show = check_number
                check_number += 1
                payment.print_show_date = check_date
                payment.first_charecter_year = (check_date[0])
                payment.second_charecter_year = (check_date[1])
                payment.third_charecter_year = (check_date[2])
                payment.fourth_charecter_year = (check_date[3])
                payment.first_charecter_month = (check_date[5])
                payment.second_charecter_month = (check_date[6])
                payment.first_charecter_day = (check_date[8])
                payment.second_charecter_day = (check_date[9])
                payment.reacivie_print_date = check_date
            return payments.do_print_checks_bd()