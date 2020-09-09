from odoo import api, _, models, fields
from datetime import date


class KsStudentClass(models.Model):
    _name = 'ks.student.class'
    # _rec_name = 'ks_student_id'
    _description = 'Student Class'

    name = fields.Char(string="Code", readonly=True, required=True, copy=False, default='New')
    ks_student_id = fields.Many2one('ks.student', 'Student ID', required=True)
    ks_class_id = fields.Many2one('ks.class', 'Class', required=True)
    ks_division_id = fields.Many2one('ks.division', 'Class Division', required=True)
    ks_year_id = fields.Many2one('ks.school.year', 'Year', required=True)
    ks_subjects_ids = fields.One2many('ks.student.subject', 'ks_subject_id', 'Subject')

    # _sql_constraints = [
    #     ('ks_stu_id_uniq', 'unique (ks_student_id)', 'Student ID must be unique!'), ]

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            ks_roll_number = self.env['ks.student'].browse([vals.get('ks_student_id')]).ks_roll_number
            ks_stu_class = self.env['ks.class'].browse([vals.get('ks_class_id')]).name
            vals['name'] = ks_roll_number + '-' + ks_stu_class
        result = super(KsStudentClass, self).create(vals)
        return result
