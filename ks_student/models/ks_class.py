from odoo import api, _, models, fields
from datetime import date


class KsClass(models.Model):
    _name = 'ks.class'
    _description = 'Class'

    name = fields.Char('Class Name', required=True)
    name_sequence = fields.Char(string="Code", readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code('ks.class.code') or _('New')
        result = super(KsClass, self).create(vals)
        return result
