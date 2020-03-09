# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words

class PrintCheck(models.Model):

    _inherit = 'account.payment'
    
    def do_print_checks_bd(self):
        if self:
            check_layout = self[0].company_id.account_check_printing_layout
            # A config parameter is used to give the ability to use this check format even in other countries than US, as not all the localizations have one
            if check_layout != 'disabled' and check_layout == 'action_print_check_bd':
                self.write({'state': 'sent'})
                return self.env.ref('meta_payment_check.%s' % check_layout).report_action(self)
        return super(PrintCheck, self).do_print_checks_bd()
    
    
    
    # and (self[0].journal_id.company_id.country_id.code == 'US' or bool(self.env['ir.config_parameter'].sudo().get_param('account_check_printing_force_us_format')))