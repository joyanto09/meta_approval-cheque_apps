# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class PurchaseOrder(models.Model):
    
    _inherit = 'purchase.order'


    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'RFQ Sent'),
        ('first_approval', 'Internal Audit Approval'),
        ('second_approval', 'BPO Approval'),
        ('third_approval', 'Head of Procurement Approval'),
        ('fourth_approval', 'CEO Approval'),
        ('to approve', 'Approved'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)


    def operation_send_approve(self):
        
        try:
            
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            ref = self.name
            
            if not self.env['mail.channel'].search([('name','=','Purchase Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Purchase Approval Notification','public':'public', 'group_ids': users_group})
            purchase_message= self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            purchase_message.message_post(
            subject='testing',
            body='''Operattor Sent a Purchase Approval To Internal Audit,, Purchase Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'first_approval'})
    # def operation_send_approve(self):
    #     return self.write({'state': 'first_approval'})
    

    def first_approval(self):
        
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Internal Audit Approved Purchase Order ,, Purchase Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'second_approval'})
    # def first_approval(self):
    #     return self.write({'state': 'second_approval'})
    
    def first_approval_reject(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Internal Audit Canceled Purchase Order,, Canceled Purchase Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def second_approval(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''BPO Approved Purchase Order,, Purchase Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')

        except:
            pass

        return self.write({'state': 'third_approval'})
    # def second_approval(self):
    #     return self.write({'state': 'third_approval'})
    
    def second_approval_reject(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''BPO Canceled Purchase Order,, Canceled Purchase Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def third_approval(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Procurement Approved Purchase Order,, Purchase Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        except:
            pass

        return self.write({'state': 'fourth_approval'})
    # def third_approval(self):
    #     return self.write({'state': 'fourth_approval'})
    
    def third_approval_reject(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Procurement Canceled Purchase Order,, Canceled Purchase Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def fourth_approval(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Approved Purchase Order,, Purchase Order Approval NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'to approve'})
    # def fourth_approval(self):
    #     return self.write({'state': 'to approve'})
    
    def fourth_approval_reject(self):
        try:
            
            ref = self.name

            channel_id = self.env['mail.channel'].search([('name','=','Purchase Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Canceled Purchase Order,, Canceled Purchase Order NO: ''' +" "+ ref,
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancel'})
    
    def button_confirm(self):

        for order in self:
            if order.state not in ['draft', 'sent', 'to approve',]:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step'\
                    or (order.company_id.po_double_validation == 'two_step'\
                        and order.amount_total < self.env.company.currency_id._convert(
                            order.company_id.po_double_validation_amount, order.currency_id, order.company_id, order.date_order or fields.Date.today()))\
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True


    

       
    
        
    