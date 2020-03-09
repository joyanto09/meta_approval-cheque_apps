# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from num2words import num2words

class res_company_bd(models.Model):
    _inherit = "res.company"
    
    account_check_printing_layout = fields.Selection(string="Check Layout", required=True,
        help="Select the format corresponding to the check paper you will be printing your checks on.\n"
             "In order to disable the printing feature, select 'None'.",
        selection=[
            ('disabled', 'None'),
            ('action_print_check_top', 'check on top'),
            ('action_print_check_middle', 'check in middle'),
            ('action_print_check_bottom', 'check on bottom'),
            ('action_print_check_bd', 'check on BD'),
        ],
        default="action_print_check_bd")