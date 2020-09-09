from odoo import api, _, models, fields
from datetime import date


class KsStudent(models.Model):
    _name = 'ks.student'
    _description = 'Student'

    ks_roll_number = fields.Char('Roll Number', readonly=True, required=True, copy=False, default='New')
    name = fields.Char('Student Name', required=True)
    ks_dob = fields.Date('Date Of Birth', required=True)
    ks_age = fields.Integer('Age', compute='ks_calculate_age')
    ks_address = fields.Char('Address')
    ks_parent_name_id = fields.Many2one('res.partner', 'Parent Name', required=True)
    ks_student_history_ids = fields.One2many('ks.student.class', 'ks_student_id', string='Student History')

    # Fields for address
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    mobile = fields.Char('Mobile')

    @api.model
    def create(self, vals):
        if vals.get('ks_roll_number', _('New')) == _('New'):
            vals['ks_roll_number'] = self.env['ir.sequence'].next_by_code('roll.number.sequence') or _('New')
        result = super(KsStudent, self).create(vals)
        return result

    @api.onchange('ks_dob')
    def ks_calculate_age(self):
        for rec in self:
            ks_days_in_year = 365.2425
            ks_birth_date = rec.ks_dob
            if ks_birth_date:
                rec.ks_age = int((date.today() - ks_birth_date).days / ks_days_in_year)

