from datetime import date
from odoo import api, _, models, fields
from odoo.exceptions import UserError, ValidationError


class KsSchoolYear(models.Model):
    _name = 'ks.school.year'
    _description = 'School Year'

    name = fields.Char('School Year', required=True)
    ks_start_date = fields.Date('School Start Year', required=True)
    ks_end_date = fields.Date('School End Year', required=True)
    is_current_year = fields.Boolean("Current Year", compute='ks_current_year')

    _sql_constraints = [
        ('school_year_name_uniq', 'unique (name)', 'Each School Year must be unique!'),
    ]

    def ks_current_year(self):
        for rec in self:
            ks_today_date = date.today()
            ks_start_date = rec.ks_start_date
            ks_end_date = rec.ks_end_date
            if (ks_today_date >= ks_start_date) and (ks_today_date <= ks_end_date):
                rec.is_current_year = True
            else:
                rec.is_current_year = False

    @api.onchange('ks_start_date', 'ks_end_date')
    def ks_check_school_overlap_year_date(self):
        ks_start_date = self.ks_start_date
        ks_end_date = self.ks_end_date
        if ks_start_date and ks_end_date:
            if (ks_end_date.year > ks_start_date.year) and (ks_end_date.month < ks_start_date.month):
                raise ValidationError(_("End Date Should Be next Year of Start Year"))
            # ks_overlap_year = (ks_end_date - ks_start_date).days + 1
            # if ks_overlap_year == 366:
            #     if ks_end_date.year % 4 == 0:
            #         ks_overlap_year -= 1
            #     elif ks_start_date % 4 == 0:
            #         ks_overlap_year -= 1
            # if ks_overlap_year != 365:
            #     raise ValidationError(_("End Date Should Be next Year of Start Year"))

