from odoo import fields, models

class PaymentReceipt(models.Model):
    _inherit = 'account.payment'
    
    receipt = fields.Binary('Recibo de pago')