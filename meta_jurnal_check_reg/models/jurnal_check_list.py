from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class jurnal_check_list(models.Model):
    _name = "jurnal.check.list"
    _description = "Journal Check List"

    journal_check_no = fields.Char(string="Check Number")
    journal_check_amount = fields.Float(string="Amount")
    journal_check_ref_name = fields.Char(string="Partner")
    journal_check_type = fields.Char(string="Check Type")
    journal_check_id = fields.Char(string="Journal ID")

    journal_check_print_date = fields.Char(string="Check Print Date")
    journal_name = fields.Char(string="Number")