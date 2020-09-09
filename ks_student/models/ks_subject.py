from odoo import api, _, models, fields
from datetime import date


class KsSubject(models.Model):
    _name = 'ks.subject'
    _description = 'Subject'

    name = fields.Char('Subject Name', required=True)
    name_sequence = fields.Char(string="Code", readonly=True, required=True, copy=False, default='New')

    @api.model
    def create(self, vals):
        if vals.get('name_sequence', _('New')) == _('New'):
            vals['name_sequence'] = self.env['ir.sequence'].next_by_code('ks.subject') or _('New')
        result = super(KsSubject, self).create(vals)
        return result
