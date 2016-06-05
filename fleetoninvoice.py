# -*- coding: utf-8 -*- #
from openerp import models, fields, api


class FleetOnInvoiceTask(models.Model):
    _inherit = 'account.invoice'
    fleet_invoice_id = fields.Many2one('fleet.vehicle', 'Fleet')
    fleet_invoice_odometer = fields.Float(compute='_get_odometer_from_id', readonly=True, string='Odometer status')
    fleet_invoice_real_odometer = fields.Many2one('fleet.vehicle.odometer', 'Odometer', help='Odometer measure of the vehicle at the moment of this invoice', readonly=True, states={'draft': [('readonly', False)]})

    @api.one
    def _get_odometer_from_id(self):
        if self.fleet_invoice_real_odometer.value:
            self.fleet_invoice_odometer = self.fleet_invoice_real_odometer.value
        elif not self.fleet_invoice_real_odometer and self.fleet_invoice_id and self.fleet_invoice_id.odometer:
            self.fleet_invoice_odometer = self.fleet_invoice_id.odometer
        else:
            self.fleet_invoice_odometer = 0

    @api.onchange('fleet_invoice_real_odometer')
    def _onchange_fleet_invoice_real_odometer(self):
        if self.fleet_invoice_real_odometer:
            self.fleet_invoice_odometer = self.fleet_invoice_real_odometer.value
            self.fleet_invoice_id = self.fleet_invoice_real_odometer.vehicle_id


