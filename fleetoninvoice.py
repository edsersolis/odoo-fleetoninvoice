# -*- coding: utf-8 -*- #
from openerp import models, fields, api
class FleetOnInvoiceTask(models.Model):
    _inherit = 'account.invoice'
    fleet_invoice_id = fields.Many2one('fleet.vehicle', 'Fleet')
    fleet_invoice_odometer = fields.Float(string='Odometer', related='fleet_invoice_id.odometer')
