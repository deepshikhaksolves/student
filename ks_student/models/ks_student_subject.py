from odoo import api, models, fields
from datetime import date


class KsStudentSubject(models.Model):
    _name = 'ks.student.subject'
    _rec_name = 'ks_subject_id'
    _description = 'Student Subject'

    ks_subject_id = fields.Many2one('ks.subject', 'Subject ID')
    ks_student_class_id = fields.Many2one('ks.student.class', 'Class ID')

    # _sql_constraints = [
    #     ('ks_stu_class_id_uniq', 'unique (ks_student_class_id)', 'Student Class ID must be unique!'), ]
