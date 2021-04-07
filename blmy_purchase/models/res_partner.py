# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    category_type = fields.Selection([
        ('assy', 'ASSY'),
        ('cots', 'COTS'),
        ('fab', 'FAB'),
        ('other', 'OTHER'),
        ('undefined', 'UNDEFINED')
    ], 'Vendor Category Type', required=False)
    last_date_reviewed = fields.Date('Last Date Reviewed')
    account_status = fields.Selection([
        ('active', 'Active'),
        ('dormant', 'Dormant'),
        ('inactive', 'Inactive')
    ], 'Vendor Account Status', required=False)
    approval_status = fields.Selection([
        ('approved', 'Approved'),
        ('customer_required', 'Customer Required'),
        ('probationary', 'Probationary'),
        ('prohibited', 'Prohibited'),
        ('single_use', 'Single Use')
    ], 'Approval Status', required=False)
    account_number = fields.Char('Account Number')

    @api.model
    def create(self, vals):
        self.correct_state(vals)
        return super(res_partner, self).create(vals)

    @api.model
    def write(self, vals):
        self.correct_state(vals)
        return super(res_partner, self).write(vals)

    @api.model
    def correct_state(self, vals):
        if vals.get('state_id', False):
            current_state = self.env['res.country.state'].browse(vals['state_id'])
            if current_state.country_id.code != 'US':
                state_code = current_state.code
                state = None
                if vals.get('country_id', False):
                    state = self.env['res.country.state'].search(
                        [("code", "=", state_code), ('country_id', '=', vals['country_id'])])
                if not state or not state.id:
                    us_ctry = self.env['res.country'].search([('code', '=', 'US')], limit=1)
                    state = self.env['res.country.state'].search(
                        [("code", "=", state_code), ('country_id', '=', us_ctry.id)])
                if not state or not state.id:
                    state = current_state

                vals['state_id'] = state.id
                vals['country_id'] = state.country_id.id
            else:
                vals['country_id'] = current_state.country_id.id





