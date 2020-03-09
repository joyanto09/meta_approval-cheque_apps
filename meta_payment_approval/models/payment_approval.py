# -*- coding: utf-8 -*-
from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class AccountPaymentApproval(models.Model):

    _inherit = 'account.payment'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('first_approval', 'Manager Approval'),
        ('second_approval', 'Head of Finance Approval'),
        ('third_approval', 'CEO Approval'),
        ('approve', 'Approved'),  
        ('posted', 'Validated'), 
        ('sent', 'Sent'), 
        ('reconciled', 'Reconciled'), 
        ('cancelled', 'Cancelled'), 
        ], readonly=True, default='draft', copy=False, string="Status")
    
    
    def payment_set_for_approval(self):
        
        self.write({'state': 'draft'})
        return {
            "type": "ir.actions.act_window_close",
        }
        
    def operation_send_approve(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            users_group = self.env['res.groups'].search([('name','=','Internal User')])
            # ref = self.name
            
            users.notify_success("Operator Sent a Payments Approval To Manager,,")
            
            if not self.env['mail.channel'].search([('name','=','Payments Approval Notification')]):
                self.env['mail.channel'].create({'name': 'Payments Approval Notification','public':'public', 'group_ids': users_group})
            payments_message= self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            payments_message.message_post(
            subject='testing',
            body='''Operattor Sent a Payments Approval To Manager,,''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'first_approval'})
    
    def first_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("Manager Approved a Payments ,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Manager Approved a Payments ,, & Approval Sent To Head of Finance ''',
            subtype='mail.mt_comment')
        
        except:
            pass
        
        return self.write({'state': 'second_approval'})
    
    def first_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("Manager Canceled a Payments,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Manager Canceled a Payments,,,''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancelled'})
    
    def second_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("Head of Finance Approved a Payments ,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Finance Approved a Payments ,, & Approval Sent To CEO ''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'third_approval'})
    
    def second_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("Head of Finance Canceled a Payments,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''Head of Finance Canceled a Payments,,,''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancelled'})
    
    def third_approval(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_success("CEO Approved a Payments ,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Approved a Payments ,, & Now a Payments Approved ''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'approve'})
    
    def third_approval_reject(self):
        try:
            users=self.env['res.users'].search([('active','=',True)])
            # ref = self.name
            users.notify_info("CEO Canceled a Payments,, ")

            channel_id = self.env['mail.channel'].search([('name','=','Payments Approval Notification')])

            channel_id.message_post(
            subject='testing',
            body='''CEO Canceled a Payments,,,''',
            subtype='mail.mt_comment')
        
        except:
            pass

        return self.write({'state': 'cancelled'})
    
    
    def post(self):
        """ Create the journal items for the payment and update the payment's state to 'posted'.
            A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
            and another in the destination reconcilable account (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
        """
        AccountMove = self.env['account.move'].with_context(default_type='entry')
        for rec in self:

            if rec.state != 'approve':
                raise UserError(_("Only a draft payment can be posted."))

            if any(inv.state != 'posted' for inv in rec.invoice_ids):
                raise ValidationError(_("The payment cannot be processed because the invoice is not open!"))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    if rec.partner_type == 'customer':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.customer.invoice'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.customer.refund'
                    if rec.partner_type == 'supplier':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.supplier.refund'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.supplier.invoice'
                rec.name = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=rec.payment_date)
                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))

            moves = AccountMove.create(rec._prepare_payment_moves())
            moves.filtered(lambda move: move.journal_id.post_at != 'bank_rec').post()

            # Update the state / move before performing any reconciliation.
            move_name = self._get_move_name_transfer_separator().join(moves.mapped('name'))
            rec.write({'state': 'posted', 'move_name': move_name})

            if rec.payment_type in ('inbound', 'outbound'):
                # ==== 'inbound' / 'outbound' ====
                if rec.invoice_ids:
                    (moves[0] + rec.invoice_ids).line_ids \
                        .filtered(lambda line: not line.reconciled and line.account_id == rec.destination_account_id)\
                        .reconcile()
            elif rec.payment_type == 'transfer':
                # ==== 'transfer' ====
                moves.mapped('line_ids')\
                    .filtered(lambda line: line.account_id == rec.company_id.transfer_account_id)\
                    .reconcile()

        return True
    
    
    # def set_to_draft(self):
    #     return self.write({'state': 'draft'})
    
    # def action_quotation(self):
    #     return self.write({'state': 'set'})
    
        # ('set', 'Payment Quotation'),