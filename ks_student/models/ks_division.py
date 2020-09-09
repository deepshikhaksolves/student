from odoo import api, _,  models, fields
from datetime import date


class KsDivision(models.Model):
    _name = 'ks.division'
    _description = 'Class Division'

    name = fields.Char('Division', required=True)
    ks_class_id = fields.Many2one('ks.class', 'Class ID')
    ks_class_subject_ids = fields.One2many('ks.class.subject', 'ks_subject_id', 'Class Subject')
