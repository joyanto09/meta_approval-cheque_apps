# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

from collections import defaultdict


class PurchaseOrderChat(models.Model):
    _name = "send.message"

    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string="Name")

    # @api.onchange('state')
    # def _chating_purchases_order(self):
        
    #     payments = self.env['purchase.order'].browse(self.env.context.get('active_ids', []))

    #     channel_id = self.env['mail.channel'].search([('name','=','test_2')])

    #     for rec in channel_id:
    #         rec.message_post(
    #         subject='testing',
    #         body='''Order is in your stage,Please Check it out''',
    #         subtype='mail.mt_comment')

    #     return payments.write({'state': 'first_approval'})

