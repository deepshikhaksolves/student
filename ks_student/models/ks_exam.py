from odoo import api, models, fields
from datetime import date


class KsExam(models.Model):
    _name = 'ks.exam'
    _description = 'Exam'

    name = fields.Char('Exam Name', required=True)
    ks_class_subject_id = fields.Many2one('ks.class.subject', 'Class Subject')
    ks_school_year = fields.Many2one('ks.school.year', 'Year',
                                      domain="[('is_current_year', '=', True)]")



    # def ks_year_compute(self):
    #     ks_year = self.env['ks.school.year'].search([])
    #     for year in ks_year:
    #         if year.is_current_year:
    #             self.ks_current_year = year.name
