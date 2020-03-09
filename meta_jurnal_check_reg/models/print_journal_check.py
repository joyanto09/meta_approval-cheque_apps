# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words

class PrintCheck(models.Model):

    _inherit = 'account.move'
    
    def do_print_checks_bd(self):
        if self:
            checks_number = self.journal_check_number
            amount_check = float(self.amount_total)
            jurnal_check_ref = self.partner_id.name
            jurnal_checks_type = self.journal_check_type
            jurnal_checks_id = self.journal_id.name
            jurnal_checks_print_date = self.get_print_date
            jurnal_checks_name = self.name
            
            payments = self.env['jurnal.check.list'].browse(self.env.context.get('active_ids', []))
            payments.create({'journal_check_no': checks_number, 'journal_check_amount': amount_check, 'journal_check_ref_name': jurnal_check_ref, 
                                'journal_check_type': jurnal_checks_type, 'journal_check_id': jurnal_checks_id, 'journal_check_print_date': jurnal_checks_print_date,
                                'journal_name': jurnal_checks_name,})
                                
            return self.env.ref('meta_jurnal_check_reg.%s' % 'action_print_journal_check_bd').report_action(self)
        # return super(PrintCheck, self).do_print_checks_bd()

            