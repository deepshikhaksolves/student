from odoo import api, models, fields
from datetime import date


class KsStudentExam(models.Model):
    _name = 'ks.student.exam'
    _description = 'Student Exam'

    name = fields.Char('Exam Name', required=True)
    ks_student_id = fields.Many2one('ks.student', 'Student ID', required=True)
    ks_student_class_id = fields.Many2one('ks.student.class', 'Student Class ID', required=True)
    ks_exam_id = fields.Many2one('ks.class.subject', 'Exam ID', required=True)

    ks_obtained_marks = fields.Integer('Obtained Marks', required=True)

    @api.onchange('ks_student_class_id')
    def ks_exam_id_domain(self):
        for rec in self:
            return {'domain':  {'ks_exam_id': [('ks_student_class_id', '=', rec.ks_student_class_id.id)]}}

