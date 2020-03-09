# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('first_approval', 'Head of Marketing Approval'),
        ('second_approval', 'Head of Finance Approval'),
        ('third_approval', 'COO Approval'),
        ('fourth_approval', 'CEO Approval'),
        ('to approve', 'Approved'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    
    def sale_operation_send_approval(self):
        try:
            
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            ref = self.name
            

            if not self.env['mail.channel'].search([('name','=','Sales Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Sales Approval Notification','public':'public', 'group_ids': users_group})
            purchase_message= self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            purchase_message.message_post(
            subject='testing',
            body='''Operattor Sent a Sales Approval To Head of Marketing,, Sales Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'first_approval'})
    
    def first_approval(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Marketing Approved Sales Order ,, Sales Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'second_approval'})

    def first_approval_reject(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Marketing Canceled Sales Order,, Canceled Sales Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def second_approval(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Finance Approved Sales Order ,, Sales Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'third_approval'})

    def second_approval_reject(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Finance Canceled Sales Order,, Canceled Sales Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def third_approval(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''COO Approved Sales Order ,, Sales Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'fourth_approval'})

    def third_approval_reject(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''COO Canceled Sales Order,, Canceled Sales Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    def fourth_approval(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Approved Sales Order ,, Sales Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'to approve'})

    def fourth_approval_reject(self):
        try:
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Sales Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Canceled Sales Order,, Canceled Sales Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})

    